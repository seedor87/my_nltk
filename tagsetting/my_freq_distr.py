# -*- coding: utf-8 -*-

import nltk
from prettytable import PrettyTable

def get_pos_tags(text):
    return nltk.pos_tag(text)

def process_string(text, n=50):

    _text = text.decode('utf-8').strip()
    fd = nltk.FreqDist([word.lower() for word in nltk.word_tokenize(_text)])
    return fd.most_common(n)

def process_url(url, n=50):

    import urllib
    from bs4 import BeautifulSoup

    html = urllib.urlopen(url).read().decode('utf8')
    text = BeautifulSoup(html, "lxml").get_text()
    fd = nltk.FreqDist(word.lower() for word in nltk.word_tokenize(text))
    return fd.most_common(n)


def process_file(file, n=50):

    import re

    def get_text(file):
        """Read text from a file, normalizing whitespace and stripping HTML markup."""
        text = open(file).read()
        text = re.sub(r'<.*?>', ' ', text)
        text = re.sub('\s+', ' ', text)
        return text

    string = get_text(file)
    string = string.decode('utf-8').strip()
    fd = nltk.FreqDist(word.lower() for word in nltk.word_tokenize(string))
    return fd.most_common(n)

text = """
    Graph Database Evaluation and Reference Implementation
    Executive Summary
    A graph database is a database that uses graph structures for queries with nodes, relationships and properties to represent and store data.   Within graph databases, the relationship (and its subsequent properties), is just as important as the node itself.   This relationship allows data in each node to be directly coupled in a unique way, decreasing the time and complexity required to gather associated pieces of information that are related to the object in question.  The relationships contain their own metadata, which is used as part of the query process, providing another layer of filtering for the data queries and results.
    It is with these relationships that graph databases differ from conventional relational databases.  Relational databases store their relationship links in the data itself.  Queries searching for associated data need to traverse the data store and use the JOIN concept to collect the related data.  Depending on the size of the information and the number of associations one needs to manage, relational database implementations can lead to complex and time consuming queries.  Maintaining such a store as associations come and go can also be a tedious task within a relational database.  Graph databases, by design, allow simple and rapid retrieval of complex hierarchical structures that are difficult to model in relational systems.
    Background
    The increased power, capabilities and adoption rates of computers and communications systems are generating exponentially increasing amounts of data.  Within the C4 intelligence pworld that data needs to analyzed for significant events, data or patterns to counter threats, stop the spread of disease and provide resource support to name a few.  In most cases information is collected and managed in stovepipes.  That information is then analyzed by experts within that stovepipe and decisions are made based on that data.  Unfortunately, by ponly using one stream of information, pieces of information may be missing from the overall decision process, especially if that missing information is from a totally different domain altogether.  For example, an analyst reviewing satellite data may be missing weather service and social media information that could better round out the decision process.  In many cases an analyst may have access to multiple feeds of information and will have to establish relationships between that information such as time and location to provide a more rounded out view of the item of interest.
    This leads us to why we want to explore Graph databases.  Imagine an analyst trying to manage information based on a multitude of people, places and things while also trying to establish and maintain information relationships to those objects at the same time within a relational database.  The tables and queries would constantly be changing to accommodate new information (both existing and new formats) coming and going.  The timeliness of retrieving the necessary information from such data store, that could be distributed, would
    become problematic over time.  Another issue would be completeness of the data as knowing whether all the associations are accounted for would be difficult to determine.  Graph databases appear to solve these issues by decoupling the data from the relationship and in turn aligning properties with the relationships so the information and its metadata can be view and queried based on the objects of interest solely.
    Tasking
    As part of this effort we would like the team to focus on two areas:  An evaluation of prominent graph databases to determine a viable approach to meet the needs of the above scenarios and a reference implementation that demonstrates the strength of such a database in a domain with multiple disparate data feeds.  A breakdown of the task is as follows:
    Evaluate a few prominent  Graph DB implementations (Neo4j is a popular one) and identify/document pros/cons based on the following criteria:
    Performance - how the database under varying conditions
    Organization – how is the information retained, is this different between products
    Scaling – How do the products handle scaling up data content and complexity of queries
    Cost – What is the cost/licensing approach for each product.  Which are free…but do they have a license constraint.
     Robustness of query language – How flexible is the language to perform simple to complex queries and is it easy to understand.
    Utilization – Who’s using it and on what products?
    Support – Is the product maintained, how often are updates produced?
    Product configurations - can the product support a web/cloud solution, standalone, networked, clusters?
    Services  - backup, clustering support, security, etc
    Visualization solutions – Can we easily visualize the data via a plugin or third party solution or do we have to implement our own solution? (e.g. Keyline looked like they had some solutions)
    Notification of changes – How does one get notified by changes to the data pfrom the database product.
    Batch updates – Does the product support a batch update model or is a single transaction at a time?
     Data interoperability – What level of data conditioning needs to happen before it can be stored in the database?  For example, relational databases require the user to populate a defined schema layout; ORM is based on a predefined annotated class.  Is it name value pairs, etc?  How flexible is it to handling new data types/formats?
    Space utilization – Does the product use some kind of data compression?
    Transaction support – Does the product support this?
    “Time machine analysis” - The ability to look back in time at the data and potentially update it to see how actionable data has changed.
    Pick one and define an approach to utilizing the database in both local and web/cloud based deployment environments.
    Build reference implementations of a graph database supporting a C4 intelligence based problem.  Utilize disparate data points to build relationships that can be used to build actionable activity detection.  Possibly use data from resources such as data.gov as feeds.  Do we have any other data we can point them to?
    Establish approaches for identifying/establishing relationships between the various disparate data feeds (e.g. time, location, name, etc).


    All developed artifacts are to be stored on Github.
    Goals
    Evaluate a few Graph DB solutions and document in a white paper comparative details and how each DB performed against the above criteria.
    A selected “best of breed” graph database to meet our C4 Intelligence needs (multiple disparate data feeds, some with significant volume).
    A reference implementation of that database against a C4 Intelligence based scenario that showcases the value of graph databases within that community for the management of disparate data as well as the efficient deduction of action information, due to the relationships, of that data.
    Recommendations for how to identify and build relationships from the data feeds.
    """

pt = PrettyTable()
pt.add_column("String Run", process_string(text))
pt.add_column("File Read Run", process_file('GraphDatabaseEvaluationandImplementationCon-ops.txt'))
pt.add_column("URL Test", process_url(url="http://www.archives.gov/exhibits/charters/constitution_transcript.html"))
pt.add_column("TXT File Test", process_file('gen_doc_tagset.py'))
print pt
