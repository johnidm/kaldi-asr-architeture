# Kaldi ASR Architeture Proposal

This repository contains a proposal for a speech recognition solution based on [Kaldi ASR](https://kaldi-asr.org/).

There are two main parts involved:

- Model training: the file `Dockerfile.train` includes the steps for training a model.
- Server API: the file `Dockerfile.api` sets up a REST API for consuming a trained model.

Benefits:

- Training a new model is simple.
- Consuming a trained model via a REST API is also simple.
- All artifacts are produced using [Docker](https://www.docker.com/) files.

How to train a model:

```
docker build -f Dockerfile.train -t iara-train/latest .
docker run -v $PWD/model:/model --rm -it iara-train/latest
```

> The training process may take a long time, about 12 hours.

How to consume a model:

```
docker build -f Dockerfile.api -t iara-api/latest .
docker run --rm -p 8000:8000 -it iara-api/latest
```

> The transcription endpoint is avaliable at http://localhost:8000/transcribe.

Sample transcript request

```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "url": "https://raw.githubusercontent.com/johnidm/kaldi-asr-architeture/master/audio.wav" 
}' \
 'http://127.0.0.1:8000/transcribe'
```

Sample transcript response

```
{
"elapsed_time": "0:00:24.651320",
"transcription": "esta é a da república federativa do brasil triangular las representantes da empresa brasileira é o em assembleia nacional constituinte eleita instituir o estado democrático ..."
}
```

---

Don't forget to visit the [Kaldi ASR documentation](https://kaldi-asr.org/doc/).

The [alphacep git repo](https://github.com/alphacep) contains several interesting projects involving Kaldi ASR. 

The [FalaBrasil scripts for Kaldi](https://gitlab.com/fb-asr/fb-am-tutorial/kaldi-am-train) is a set of scripts to help creating a Kaldi ASR model for Brazilian Portuguese.

Feel free to make suggestions or contributions to the project.

I hope these ideias can be helpful!
