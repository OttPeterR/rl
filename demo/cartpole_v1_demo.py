# Demo taken (adn adapted from) from the OpenAI Gym homepage

import gym
env = gym.make("CartPole-v1")
observation = env.reset()
for _ in range(42):
  env.render()
  action = env.action_space.sample() # this takes random actions
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()
print("Cool, it works!")