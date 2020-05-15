#!/bin/sh

set -e

export KALDI_IARA_DIR_PROJECT=/opt/kaldi/egs/iara
export KALDI_IARA_DIR_PROJECT_MODEL=/iara-model

export IARA_DIR_MODEL=$PWD/iara-model

echo "Iniciando treino"
echo "Diretório do modelo $KALDI_IARA_DIR_PROJECT_MODEL"

cd $ROOT_PATH/kaldi-am-train
./prep_train.sh ${KALDI_IARA_DIR_PROJECT}

cd ${KALDI_IARA_DIR_PROJECT}/s5/
./run.sh

cd $ROOT_PATH/kaldi-am-train/online
./prep_vosk.sh $KALDI_IARA_DIR_PROJECT $KALDI_IARA_DIR_PROJECT_MODEL

echo "Treino concluído"
