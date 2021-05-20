import os.path
import wget
import gzip
import shutil


def folders_creation():
    if not os.path.isdir("datasets/"):
        os.mkdir("datasets/")

    if not os.path.isdir("datasets/name.basics/"):
        os.mkdir("datasets/name.basics/")

    if not os.path.isdir("datasets/title.basics/"):
        os.mkdir("datasets/title.basics/")

    if not os.path.isdir("datasets/title.principals/"):
        os.mkdir("datasets/title.principals/")


def data_verification():
    if os.path.isfile("datasets/name.basics/data.tsv"):
        os.remove("datasets/name.basics/data.tsv")

    if os.path.isfile("datasets/title.basics/data.tsv"):
        os.remove("datasets/title.basics/data.tsv")

    if os.path.isfile("datasets/title.principals/data.tsv"):
        os.remove("datasets/title.principals/data.tsv")


def data_download():
    name_basics = wget.download("https://datasets.imdbws.com/name.basics.tsv.gz", out="datasets/name.basics/")
    title_basics = wget.download("https://datasets.imdbws.com/title.basics.tsv.gz", out="datasets/title.basics/")
    title_principals = wget.download("https://datasets.imdbws.com/title.principals.tsv.gz", out="datasets/title.principals/")

    with gzip.open(name_basics, "rb") as input:
        with open("datasets/name.basics/data.tsv", "wb") as output:
            shutil.copyfileobj(input, output)
    os.remove("datasets/name.basics/name.basics.tsv.gz")

    with gzip.open(title_basics, "rb") as input:
        with open("datasets/title.basics/data.tsv", "wb") as output:
            shutil.copyfileobj(input, output)
    os.remove("datasets/title.basics/title.basics.tsv.gz")

    with gzip.open(title_principals, "rb") as input:
        with open("datasets/title.principals/data.tsv", "wb") as output:
            shutil.copyfileobj(input, output)
    os.remove("datasets/title.principals/title.principals.tsv.gz")
