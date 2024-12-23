from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv
load_dotenv()

crew_ai = Crew(
    agents=[blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process= Process.sequential,
    memory= True,
    cache= True,
    max_rmp = 100,
    share_crew = True

)

result = crew_ai.kickoff(inputs={"topic": "Why did British hide its Gold in Canada?"})
print(result)

