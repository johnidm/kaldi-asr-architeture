# Proposal Kaldi ASR Architeture

Nesse repositório você vai encontrar uma proposta de arquiteura para uma solução de speech recognition usando o Kaldi ASR. 

Essa solução abrange duas etapas:

- Treino de um modelo: vocé encontra no arquivo `Dockerfile.train` as etapas para treinar um modelo no formado [nnet3](http://kaldi-asr.org/doc/dnn3.html) para ser consumido pelo [Kaldi ASR](http://kaldi-asr.org/).
- API para clientes: no arqivo `Dockerfile.api` você tem um exemplo de como consumir o modelo treinado em uma API REST usando o projeto [Vosk](https://github.com/alphacep/vosk-api).

Beneficios dessa arquitetura:

- Etapa de treino de um novo modelo é fácil e sem complicações.
- O modelo treinado fica disponível em uma API REST para ser consumido por clientes.
- Todos os rescursos criados estão em imagens Docker facilitando a partabilidade e manutenção do projeto.


How to train a model:
```
docker build -f Dockerfile.train -t iara-train/latest .
docker run -v $PWD/iara-model:/iara-model --rm -it iara-train/latest
```

> O treino de um novo modelo pode levar muitas horas.

How o use a model
```
docker build -f Dockerfile.api -t iara-api/latest .
docker run --rm -it iara-api/latest
```

> Acesso endereço http://localhost:5000/transcribe


If you want to learn more about ASR, I recommend [this course](https://www.edx.org/course/speech-recognition-systems-2).

Don't forget to vist [Kaldi ASR documentation](https://kaldi-asr.org/doc/)

The [alphacep git repo](https://github.com/alphacep) tem vários projeto interessantes project envolta do Kaldi ASR specialment o [Vosk API](https://github.com/alphacep/vosk-api)

The [FalaBrasil scripts for Kaldi](https://gitlab.com/fb-asr/fb-am-tutorial/kaldi-am-train) is set of scripts to create a model for Kaldi ASR for portuguese Brazil.

Sinta-se a vontade para fazer sugestões de melhorias no projeto abrindo um PR.

I hope this structure help you!  
