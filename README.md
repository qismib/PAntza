# S.P.Q.R. (Superbus Pulsorum Quantisticum Resopitorum)
PulseVQE Thesis Repository.
Questa repository contiene i codici ed i materiali associati alla tesi triennale in Fisica presso l'Università Milano Bicocca dello studende Riccardo Marega.
Il codice caricato sarà ripartito principalmente all'interno delle cartelle notebooks e scripts. La prima di queste conterrà un numero limitato di juputer notebooks ma rappresentativi delle conoscenze correnti dello studente. Nella seconda saranno invece riportati scripts python contenenti frammenti di codice appartenenti a programmi eventualmente caricati nella cartella notebooks.

## Qiskit e PulsedVQE

La pulsedVQE è implementata utilizzando [Qiskit](https://qiskit.org/), una libreria open-source di sviluppo software per calcolatori quantistici IBM. Qiskit fornisce gli strumenti necessari per progettare, simulare ed eseguire algoritmi quantistici su computer quantistici reali o simulatori.

Per ulteriori dettagli sulla pulsedVQE, fare riferimento ai seguenti articoli e risorse:
- [Referenza sulla pulsedVQE eseguita attraverso Qiskit](https://medium.com/qiskit/enhance-variational-quantum-algorithms-with-qiskit-pulse-and-qiskit-dynamics-768249daf8dd)
- [Documentazione Qiskit](https://qiskit.org/documentation/)

## VQA
1. Forma Variazionale: I VQA utilizzano un circuito quantistico variazionale, noto anche come forma variazionale o ansatz, per codificare uno stato quantistico parametrizzato. I parametri nel circuito vengono regolati durante il processo di ottimizzazione per minimizzare una funzione di costo.

2. Misurazione Quantistica: Dopo aver preparato lo stato variazionale, il computer quantistico effettua misurazioni per estrarre informazioni sullo stato quantistico. Queste misurazioni vengono utilizzate per calcolare la funzione di costo.

3. Ottimizzazione Classica: La parte classica dell'algoritmo è responsabile dell'ottimizzazione dei parametri della forma variazionale. Regola iterativamente i parametri per minimizzare la funzione di costo, tipicamente utilizzando algoritmi di ottimizzazione classici.

4. Ripetizione e Iterazione: I passaggi da 1 a 3 vengono ripetuti fino a quando l'algoritmo converge a una soluzione che minimizza la funzione di costo. I parametri risultanti codificano la soluzione al problema di ottimizzazione.
![Credit: https://www.physics.ox.ac.uk/](VQA.png)
Credit: https://www.physics.ox.ac.uk/

## Contenuti

- `scripts/`: Contiene i file sorgente principali e file testo con alcune note dello studente.
- `graphs/`: Contiene alcuni grafici necessari come spunti di riflessione per approfondire le proprie basi teoriche.
- `notebooks/`: Jupyter notebooks per analisi dati o esperimenti.
- `librerie.txt`: Il seguente file riporta l'insieme di tutte le librerie installate nell'ambiente virtuale in cui i codici vengono compilati.
- `LICENSE`: Licenza del progetto.
- `README.md`: Questo file README.

**Studente:** [Riccrdo Marega]
**Istituzione:** [Università Milano Bicocca]
**Corso di Studio:** [Laurea triennale in Fisica]
**Anno Accademico:** [2023/2024]
  
