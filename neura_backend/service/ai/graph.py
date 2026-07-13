"""
AI graph definition.
"""

# --- IMPORTS ---
from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph
from neura_backend.service.ai.nodes.planner import plan_query
from neura_backend.service.ai.nodes.search import single_search
from neura_backend.service.ai.nodes.utils.spawn_researchers import spawn_searchers
from neura_backend.service.ai.nodes.writer import final_writer
from neura_backend.service.ai.state import State


# --- CODE ---

# Define the state graph
graph = StateGraph(State)

# Add nodes
graph.add_node('plan_query', plan_query)
graph.add_node('single_search', single_search)
graph.add_node('final_writer', final_writer)

# Define edges
graph.add_edge(START, 'plan_query')

graph.add_conditional_edges('plan_query',
                            spawn_searchers,
                            ['single_search'])

graph.add_edge('single_search', 'final_writer')

graph.add_edge('final_writer', END)

# Compile the graph
web_search_agent = graph.compile()
