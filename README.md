


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
# kaldi-asr-architeture
