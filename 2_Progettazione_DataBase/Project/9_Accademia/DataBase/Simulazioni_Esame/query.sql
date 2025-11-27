-- QUERY 1:
-- 1. Quali sono le persone con stipendio di al massimo 40000 euro [2 punti]

SELECT *
FROM persona p
WHERE p.stipendio <= 40000;

-- QUERY 2:
-- 2. Quali sono i ricercatori che lavorano ad almeno un progetto e hanno uno stipendio di al massimo 40000 [2 punti]

SELECT *
FROM attivitaProgetto ap, persona p
WHERE p.id = ap.persona
    and p.stipendio <= 40000
    and p.posizione = "Ricercatore";

-- QUERY 3:
-- 3. Qual è il budget totale dei progetti nel db [2 punti]

SELECT sum(budget)
FROM progetto;

-- QUERY 4:
--- 4. Qual è il budget totale dei progetti a cui lavora ogni persona. Per ogni persona restituire nome, cognome e budget totale dei progetti nei quali è coinvolto. [3 punti]

SELECT p.nome as nome, p.cognome as cognome, sum(pr.budget) as budget_tot
FROM persone p, progetto pr, attivitaProgetto ap
WHERE p.id = ap.persona
    and pr.id = ap.progetto
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 5:
-- 5. Qual è il numero di progetti a cui partecipa ogni professore ordinario. Per ogni professore ordinario, restituire nome, cognome, numero di progetti nei quali è coinvolto [3 punti]

SELECT p.nome as nome, p.cognome as cognome, count(ap.progetto) as numero_progetti
FROM persona p, attivitaProgetto ap
WHERE p.id = ap.persona
    and p.posizione = "Professore ordinario"
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 6:
-- 6. Qual è il numero di assenze per malattia di ogni professore associato. Per ogni professore associato, restituire nume, cognome e numero di assenze per malattia [3 punti]

SELECT p.nome as nome, p.cognome as cognome, count(a.id) as numero_assenze
FROM persona p, assenza a
WHERE p.id = a.persona
    and a.tipo = "Malattia"
    and p.posizione = "Professore Associato"
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 7:
-- 7. Qual è il numero totale di ore, per ogni persona, dedicate al progetto con id ‘5’. Per ogni persona che lavora al progetto, restituire nome, cognome e numero di ore totali dedicate ad attività progettuali relative al progetto [4 punti]

SELECT p.nome as nome, p.cognome as cognome, count(ap.oreDurata) as totale_ore
FROM persona p, attivitaProgetto ap
WHERE p.id = ap.persona
    and ap.progetto = 5
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 8:
-- 8. Qual è il numero medio di ore delle attività progettuali svolte da ogni persona. Per ogni persona, restituire nome, cognome e numero medio di ore delle sue attività progettuali (in qualsivoglia progetto) [3 punti]

SELECT p.nome as nome, p.cognome as cognome, count(ap.oreDurata) as totale_ore
FROM persona p, attivitaProgetto ap
WHERE p.id = ap.persona
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 9:
-- 9. Qual è il numero totale di ore, per ogni persona, dedicate alla didattica. Per ogni persona che ha svolto attività didattica, restituire nome, cognome e numero di ore totali dedicate alla didattica [4 punti]

SELECT p.nome as nome, p.cognome as cognome, sum(anp.oreDurata) as totale_ore
FROM persona p, attivitaNonProgettuale anp
WHERE p.id = anp.persona
    AND anp.tipo = 'Didattica'
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 10:
-- 10. Quali sono le persone che hanno svolto attività nel WP di id ‘5’ del progetto con id ‘3’. Per ogni persona, restituire il numero totale di ore svolte in attività progettuali per il WP in questione [4 punti]

SELECT p.nome as nome, p.cognome as cognome, sum(ap.oreDurata) as totale_ore
FROM persona p, attivitaProgetto ap, wp
WHERE p.id = ap.persona
    AND ap.progetto = wp.progetto
    and wp.id = 5   
    and ap.progetto = 3
GROUP BY p.id, p.nome, p.cognome;