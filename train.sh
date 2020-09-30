#!/bin/sh

set -e

export KALDI_DIR_PROJECT=/opt/kaldi/egs/iara

export KALDI_DIR_PROJECT_MODEL=/model

echo "Training is starting!"

echo "Model output directory $KALDI_DIR_PROJECT_MODEL"

cd $ROOT_PATH/kaldi-am-train
./prep_train.sh ${KALDI_DIR_PROJECT}

cd ${KALDI_DIR_PROJECT}/s5/
./run.sh

cd $ROOT_PATH/kaldi-am-train/online
./prep_vosk.sh $KALDI_DIR_PROJECT $KALDI_DIR_PROJECT_MODEL

echo "Training is complete!"
