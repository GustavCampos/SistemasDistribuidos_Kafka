# Trabalho 5 - Apache Kafka com Clients
> Gustavo Campos & Stefani Arnold

## Instalação e execução do ambiente

Antes de qualquer coisa, certifique-se de ter o Docker e o Docker Compose instalados no seu sistema.
- Instalar Engine Docker: https://docs.docker.com/engine/install/
- Instalar Docker Compose: https://docs.docker.com/compose/install/

Agora basta utilizar o compose para inicializar todos os containers:
```bash
docker compose up

# Ou para versoes mais antigas
docker-compose up 
```

Certifique-se de que todos os serviços estão funcionando corretamente:
```bash
docker compose logs -f
```
Observe os logs para garantir que os controladores e brokers Kafka iniciaram sem erros.

### Usando scripts Python
Para poder utilizar os scripts é necessário dois passos:

1. Instalar gerenciador de pacotes `pip`, é possível conferir se ele foi instalado usando o comando:
    ```bash
    pip --version
    ```
2. Instalar globalmente a biblioteca `confluent-kafka`:
    ```bash
    pip install confluent-kafka
    ```

## Configuração do ambiente (docker compose)
- **Nodos (controllers)**: 
  - Existem 3 nodos configurados como `controller-1`, `controller-2` e `controller-3`.
  - Eles atuam como o quorum de controladores para gerenciar metadados e coordenação.

- **Brokers**: 
  - Existem 3 brokers configurados: `broker-1`, `broker-2` e `broker-3`.
  - Cada broker está acessível em diferentes portas mapeadas para o host:
    - `broker-1`: localhost:29092
    - `broker-2`: localhost:39092
    - `broker-3`: localhost:49092

- **Partições e fator de replicação**: 
  - O número de partições definido para cada broker é 3 (`KAFKA_NUM_PARTITIONS`).
  - O fator de replicação definido para cada broker é 3 (`KAFKA_DEFAULT_REPLICATION_FACTOR`).

## Interação via Docker e CLI
### Enviando dados para o Kafka

1. Criando um tópico chamado `meu-topico`:
   ```bash
   docker exec -it broker-1 /opt/kafka/bin/kafka-topics.sh \
     --bootstrap-server broker-1:19092 \
     --create --topic meu-topico --partitions 3 --replication-factor 3
   ```

2. Enviando mensagens para o tópico:
   ```bash
   docker exec -it broker-1 /opt/kafka/bin/kafka-console-producer.sh \
     --broker-list broker-1:19092 \
     --topic meu-topico
   ```
   Escreva mensagens no terminal. Cada linha será enviada como uma mensagem.

### Consumindo dados (leitura) do Kafka

1. Consumindo mensagens do tópico `meu-topico`:
   ```bash
   docker exec -it broker-1 /opt/kafka/bin/kafka-console-consumer.sh \
     --bootstrap-server broker-1:19092 \
     --topic meu-topico --from-beginning
   ```

## Interação via scripts Python

- Para criar um novo tópico, execute:
  ```bash
  python3 scripts/create-topic.py <nome-do-topico>
  ```

- Para deletar um tópico existente, execute:
  ```bash
  python3 scripts/delete-topic.py <nome-do-topico>
  ```

- Para enviar mensagens para um tópico, execute:
  ```bash
  python3 scripts/write-on-topic.py <nome-do-topico>
  ```
  Digite as mensagens no terminal e pressione `Enter` para enviá-las. Digite `!q` para sair.

- Para consumir mensagens de um tópico, execute:
  ```bash
  python3 scripts/read-topic.py <nome-do-topico>
  ```


## **Considerações adicionais**
- Este setup elimina a necessidade de Zookeeper ao usar controladores dedicados para gerenciar a topologia Kafka.
- Para testar a alta disponibilidade, tente parar um dos brokers e observe como o Kafka reequilibra as partições e réplicas.
- Para acessar os serviços, você pode usar os endpoints configurados no `KAFKA_ADVERTISED_LISTENERS`.