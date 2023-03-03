

<div class="styles__repoDescription___d_zn4"><h3>Purpose</h3>
<p>This docker container is meant to be used for learning purpose for programming PySpark. It has the following components.</p>
<ul>
<li>Hadoop v3.2.1</li>
<li>Spark v2.4.4</li>
<li>Conda 3 with Python v3.7</li>
</ul>
<p>After running the container, you may visit the following pages.</p>
<ul>
<li>HDFS</li>
<li>YARN</li>
<li>Spark</li>
<li>Spark History</li>
<li>Jupyter Lab</li>
<li>Airflow</li>
</ul>
<p>Use docker image</p>
<ol>
<li>Pull docker image</li>
</ol>
<pre><code>docker pull avnish327030/spark-hadoop-airflow
</code></pre>
<ol start="2">
<li>Rename pulled docker image</li>
</ol>
<pre><code>docker image tag  avnish327030/spark-hadoop-airflow spark-hadoop-airflow
</code></pre>
<ol start="3">
<li>To run the docker image</li>
</ol>
<p>window system:</p>
<ul>
<li>[D:\Project\big_data] is the path and can be replaced based on what you want in below command or you can create this directory and use same command.</li>
</ul>
<pre><code>docker run -it -p 9870:9870 -p 8088:8088 -p 8080:8080 -p 18080:18080 -p 9000:9000 -p 8888:8888 -p 9864:9864 -p 8085:8085 -p 8793:8793 -p 8081:8081 -v D:\project\spark_etl_airflow-main\notebook:/root/ipynb -v D:\project\spark_etl_airflow-main\airflow:/home/airflow -v D:\project\spark_etl_airflow-main\data:/data avnish327030/spark-hadoop-airflow
</code></pre>
<p>Linux system</p>
<pre><code>PROJECT_DIR=$(pwd)

docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -p 8085:8085 \
    -p 8793:8793 \
    -p 8081:8081 \
    -v $PROJECT_DIR/project/notebook:/root/ipynb \
    -v $PROJECT_DIR/project/airflow:/home/airflow \
    -v $PROJECT_DIR/data:/data \
    avnish327030/spark-hadoop-airflow
</code></pre>
<p>Click on below link to access portal</p>
<p><a href="http://localhost:9870/" rel="nofollow noopener">Name Node</a></p>
<p><a href="http://localhost:8088" rel="nofollow noopener">Hadoop Cluster</a></p>
<p><a href="http://localhost:8080" rel="nofollow noopener">Spark Master</a></p>
<p><a href="http://localhost:18080" rel="nofollow noopener">History Server</a></p>
<p><a href="http://localhost:8888" rel="nofollow noopener">Jupyter lab</a></p>
<p><a href="http://localhost:9864" rel="nofollow noopener">Hadoop Data Node</a></p>
<p><a href="http://localhost:8085" rel="nofollow noopener">Airflow UI</a></p>
<p><a href="http://localhost:8081" rel="nofollow noopener">Spark Worker Node</a></p>
</div>
