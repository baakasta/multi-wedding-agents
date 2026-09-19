from prompt import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from models import groq_model
from agents import delegate_to_subagent1, delegate_to_subagent2
import logging
from langchain.messages import HumanMessage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.info("asking user for their requirements...")
user_requirements = input("Please enter your requirements and preferences for your wedding: \n")

updated_system_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements)

logging.info("initializing Main wedding planner agent...")
main_wedding_planner_agent = create_agent(model=groq_model, 
                                          tools=[delegate_to_subagent1, delegate_to_subagent2], 
                                          name="MainWeddingPlannerAgent", 
                                          system_prompt=updated_system_prompt)


logging.info("invoking Main wedding planner agent...")
main_wedding_planner_agent_response = main_wedding_planner_agent.invoke({"messages":[HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})

logging.info("\nMain Wedding Planner Agent's Response:")
print(main_wedding_planner_agent_response["messages"][-1].content)