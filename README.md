```bash
#docker build image
docker build -t analytics_image .

#docker run image
docker run -it --name bigdata library/analytics_image:latest

#docker tag image
docker tag library/analytics_image:latest mariveatef/analytics_image:latest

#docker push image
docker push mariveatef/analytics_image:latest

```

#Execution flow
1-Build docker image from Dockerfile
2-Run the container
3-Inside the container, run python scripts (python ./ingest.py adult.csv) to start the pipline:
    * Ingest save data as (`data_raw.csv`)
    * Preprocess the data (`data_preprocessed.csv`)
    * Generate insights (`insight1.txt`, `insight2.txt`, `insight3.txt`, `insight4.txt`)
    * Create visualization (`summary_plot.png`)
    * Make clusters (`clusters.txt`)
4- Exit container
5- Run `bash summary.sh` to copy all output files from container to host folder `results/` and remove the container
6. Review outputs in `results/`

###sample outputs
1-Process of the pipline in the terminal:
Ingest done
Preprocess done
Analytics done
Visualization done
Clustering done
2- Exit the container and run the `summary.sh`
All outputs copied into results folder and container removed successfully!
3- `result/` contains these :
`clusters.txt`
`summary_plot.png`
`insight1.txt`
`insight2.txt`
`insight3.txt`
`insight4.txt`
`data_preprocessed.csv`
`data_raw.csv`