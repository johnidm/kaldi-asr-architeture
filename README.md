# Kaldi ASR Architeture Proposital

In this repo I will sugerirri uma estrutura de treino e consumo de uma serviço de ASR. Of course this proposta should migrate for another Machine Leaning project desde de que you have a train process and consume service.

The key points 
- The train process and the consumer service should be  in Docker contaiier.
- Easy to execute and cusome resources, just execute a Docker run.
- All resource, including train files and consumer models should be avaliable in URLs or inside the Docker image.

O processo de desenvolvimento esta divido em duas parte, train and api.

How to train a model:
```
docker build -f Dockerfile.train -t iara-train/latest .
docker run -v $PWD/iara-model:/iara-model --rm -it iara-train/latest
```

How o use a model
```
docker build -f Dockerfile.api -t iara-api/latest .
docker run --rm -it iara-api/latest
```

If you want to learn more about ASR, I recommend [this course](https://www.edx.org/course/speech-recognition-systems-2).

Don't forget to vist [Kaldi ASR documentation](https://kaldi-asr.org/doc/)

The [alphacep git repo](https://github.com/alphacep) tem vários projeto interessantes project envolta do Kaldi ASR specialment o [Vosk API](https://github.com/alphacep/vosk-api)

The [FalaBrasil scripts for Kaldi](https://gitlab.com/fb-asr/fb-am-tutorial/kaldi-am-train) is set of scripts to create a model for Kaldi ASR for portuguese Brazil.

I hope this structure helps you a lot!  Have a great day and a great week!
