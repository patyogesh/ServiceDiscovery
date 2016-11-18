from flask import Flask, request
from enum import Enum

class ServiceTypes(Enum):
    tweet_text = 1
    hashtags = 2
    user_mentions = 3
    coordinates = 4
    created_at = 5
    retweet_count = 6
    user = 7
    track_place = 8

app = Flask(__name__)

@app.route('/')
def index():
    return "This is Home"

@app.route('/user')
def user():
    return "Welcome !!"

@app.route('/text/<topic>', methods=[ 'GET', 'POST'])
def track_text(topic):
    param_list = []
    if request.method == 'POST':
        param_list.append(topic)
        start_tracking(ServiceTypes.tweet_text, param_list)
        return 'OK, will start tracking <h2>%s</h2>' % topic

    elif request.method == 'GET':
        return ret_results(ServiceTypes.tweet_text, topic)


@app.route('/hashtag/<hashtag>', methods=['POST', 'GET'])
def track_hashtags(hashtag):
    param_list = []
    if request.method == 'POST':
        param_list.append(hashtag)
        start_tracking(ServiceTypes.hashtags, param_list)
        return "Tracking hashtag %s" % hashtag

    elif request.method == 'GET':
        return ret_results(ServiceTypes.hashtags, hashtag)


@app.route('/mentions/<user_mentioned>', methods=['GET', 'POST'])
def track_user_mentions(user_mentioned):
    param_list = []
    if request.method == 'POST':
        param_list.append(user_mentioned)
        start_tracking(ServiceTypes.user_mentions, param_list)
        return "Tracking user-mentions for %s" % user_mentioned

    elif request.method == 'GET':
        return ret_results(ServiceTypes.user_mentions, user_mentioned)

@app.route('/coordinates/<float:long>, <float:latt>', methods=['GET', 'POST'])
def coordinates(long, latt):
    param_list = []
    if request.method == 'POST':
        param_list.append(long)
        param_list.append(latt)
        start_tracking(ServiceTypes.coordinates,param_list)
        return 'Tracking tweet from %s %s' % long, latt

    elif request.method == 'GET':
        return ret_results(ServiceTypes.coordinates, " ")


@app.route('/created-at/<created_at>', methods=['GET', 'POST'])
def track_created_at(created_at):
    param_list = []
    if request.method == 'POST':
        param_list.append(created_at)
        start_tracking(ServiceTypes.created_at, param_list)
        return "Tracking tweets created at %s" % created_at

    elif request.method == 'GET':
        return ret_results(ServiceTypes.created_at, created_at)


@app.route('/retweet/<retweet_count>', methods=['GET', 'POST'])
def track_retweet_count(retweet_count):
    param_list = []
    if request.method == 'POST':
        param_list.append(retweet_count)
        start_tracking(ServiceTypes.retweet_count, param_list)
        return "Tracking retweets >= %s" % retweet_count

    elif request.method == 'GET':
        return ret_results(ServiceTypes.retweet_count, retweet_count)


@app.route('/user/<user>', methods=['GET', 'POST'])
def track_user(user):
    param_list =[]
    if request.method == 'POST':
        param_list.append(user)
        start_tracking(ServiceTypes.user, param_list)
        return "Tracking tweets from user %s" % user

    elif request.method == 'GET':
        return ret_results(ServiceTypes.user, user)


@app.route('/place/<country>', methods=['GET', 'POST'])
def track_place(country):
    param_list = []
    if request.method == 'POST':
        param_list.append(country)
        start_tracking(ServiceTypes.track_place, param_list)
        return "Tracking tweets from %s" % country

    elif request.method == 'GET':
        return ret_results(ServiceTypes.track_place, country)


def start_tracking(type, param):
    '''
    Place Holder for method that will
    1. Create new Analytics Job
    2. Identify and allocate resources
        - containers
        - network-configuration
        - lookup & create database entry
    3. Create registry entry for this analytics job

    :param type: Type of date-field in tweet to run analytics on
    :param param: Data value
    :return:
    status of newly created analytics job
    '''



def ret_results(type, param):
    '''
    This function collects the results of tracking/analytics
    done so far for the type of data-field in tweet
    :param type: Type of date-field in tweet to track
    :param param: Data value
    :return:
    '''
    return "Result for %s %s" % (type.name,param)


if __name__ == "__main__":
    app.run(debug=True)
