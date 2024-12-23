from crewai import Task
from tools import yt_tool
from agents import blog_writer

research_task = Task(
    description = (
        "identify the video {topic}"
        "get detailed information about the video from the Youtube chennel video on the {topic} and create the content for blog"),
        expected_output= "A comprehensive 3 paragraph long report based on the {topic} of the video ",
        tools=[yt_tool],
        agent=blog_writer,
        async_execution=False,
        output_file= "new-blog-post.md"
)
