#!/bin/sh
cd dynamodb_local_latest
java "-Djava.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb