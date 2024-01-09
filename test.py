import openai

completion = openai.Completion.create(
  prompt="""In the following scenario, Mr. Diop had to decide whether to accept or reject the proposal.

Scenario: Ms. Johnson is given 10$. Ms. Johnson will propose how to split the money between herself and Mr. Diop. Then Mr. Diop will decide whether to accept or reject Ms. Johnson's proposal. If Mr. Diop accepts, then Ms. Johnson and Mr. Diop get the money as they agreed to split. If Mr. Diop rejects, then Ms. Johnson and Mr. Diop both receive nothing. Ms. Johnson takes 6$ for herself and offers Mr. Diop 4$.

Answer: Mr. Diop decides to ungrammatical""",
  engine="text-davinci-003",
  max_tokens=0,
  temperature=1,
  n=1,
  logprobs=1,
  echo=True,
  presence_penalty=0,
  frequency_penalty=0,
  stop=None,
)

print(completion)