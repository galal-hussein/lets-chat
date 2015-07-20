#!/bin/bash
sleep 10
if env | grep -q ^RANCHER_CLUSTER=; then
  MONGO_CONT=`python api_rancher.py`
  export LCB_DATABASE_URI=mongodb://$MONGO_CONT/letschat
  echo $LCB_DATABASE_URI
fi 
npm start

