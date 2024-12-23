from crewai import Agent
from tools import yt_tool


## Create a blog Content Reacher
blog_researcher = Agent(
    role= "Blog Researcher from YouTube videos",
    goal="get the relevant video content {topic} from yt channel",
    verbose=True,
    memory= True,
    backstory=(
        "Expert in Understanding informative explainer videos and providing suggestion"
    ),
    tools=[yt_tool],
    allow_delegation=True


)

blog_writer = Agent(
    role= "Blog writer",
    goal = "write compelling blogs about the video {topic} from YouTube Channel",
    verbose = True,
    memory = True,
    backstory=(
        "with a flair for simplfying  complex topics into digestible and engaging content"
        "you transform complex concepts into clear and concise explainer videos"
        "engagging narrative that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=False,
)
