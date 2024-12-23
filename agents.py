from crewai import Agent


## Create a blog Content Reacher
blog_researcher = Agent(
    role= "Blog Researcher from YouTube videos",
    goal="get the relevant video content {topic} from yt channel",
    verbose=True,
    memory= True,
    backstory=(
        "Expert in Understanding informative explainer videos and providing suggestion"
    ),
    tools=[],
    allow_delegation=True


)