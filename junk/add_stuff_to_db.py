from update_state import r, get_submission_urls, get_stream_from_url, get_reddit_username, get_or_create
from app import Streamer, Submission, db


def add_streamers():
    submissions = r.get_subreddit('watchpeoplecode').get_new(limit=None)
    for s in submissions:
        for url in get_submission_urls(s):
            stream = get_stream_from_url(url, s.id)
            if stream and stream.streamer is None:
                reddit_username = get_reddit_username(s, url)
                streamer = Streamer.query.filter_by(reddit_username=reddit_username).first()
                if streamer is None:
                    streamer = Streamer(reddit_username)

                stream.streamer = streamer
                stream._update_status()

                db.session.add_all([stream, streamer])
                db.session.commit()


def add_submissions():
    submissions = r.get_subreddit('watchpeoplecode').get_new(limit=None)
    for s in submissions:
        for url in get_submission_urls(s):
            stream = get_stream_from_url(url, s.id)
            if stream:
                stream.submission = get_or_create(Submission, submission_id=s.id)