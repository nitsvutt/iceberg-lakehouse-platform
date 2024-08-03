# Lakehouse Platform

![license](https://img.shields.io/github/license/nitsvutt/lakehouse-platform)
![stars](https://img.shields.io/github/stars/nitsvutt/lakehouse-platform)
![forks](https://img.shields.io/github/forks/nitsvutt/lakehouse-platform)

## Table of Contents
1. [Introduction](#introduction)
2. [Architecture](#architecture)
3. [In progress](#in-progress)


<div id="introduction"/>

## 1. Introduction

These days, data becomes the DNA of every organization including both startups and big corporations. The more an enterprise leverages the data, the more competitive advantages it gains. After defining where are data sources, all of them always require a "single source of truth" for furthure actions, such as reporting and advance analytics. This project aims to introduce an universal solution known as a **Data Lakehouse Platform**.

<div id="architecture"/>

## 2. Architecture

<p align="center">
  <img src="https://github.com/nitsvutt/lakehouse-platform/blob/main/asset/lakehouse-platform.png" width="100%" title="architecture" alt="architecture">
</p>

- Data source: your application databases (Example: MySQL, PostgreSQL).
- Data platform:
    - Event streaming service: capture data in real-time from your sources (Example: Apache Kafka).
    - Processing service:
        - Streaming processing: consume and process data from Kafka topics (Example: Apache Spark, Apache Flink).
        - Batch processing: perform heavy ETL pipelines (Example: Apache Spark).
    - Data lakehouse:
        - Storage: play as a central repository storing your data (Example: Apache Hadoop - HDFS).
        - Table format: play as an OLAP layer supporting ACID (Example: Apache Iceberg).
    - Query engine: perform structure queries of users (Example: Trino).
    - User interface: serve users (Example: Hue, Apache Superset).
    - Other serivces:
        - Containerization: develop, ship, and run applications (Example: Docker).
        - Metadata database: store metadata for other services (Example: PostgreSQL).
        - Orchestration: author, schedule and monitor workflows (Example: Apache Airflow).

<div id="in-progress"/>

## 3. In progress