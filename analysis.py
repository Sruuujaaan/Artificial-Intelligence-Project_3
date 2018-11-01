# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
   """
        Noise refers to how often an agent ends up in an unintended successor state, when they perform an action.
        So we make Noise as almost 0 assuming agent always takes intended successor state.
        Considering ideal case where discount is 1(.9) and noise is 0(.01). So we change the values accordingly
    """
   answerDiscount = .9
   answerNoise = 0.01
   return answerDiscount, answerNoise

def question3a():
    """
        Prefer the close exit (+1), risking the cliff (-10). Kept noise at 0 to maximize the output. started discount factor at 0.2.
        Two steps to reach +1 exit. East East and North. Thus set discount factor 0.2 and living reward 0.4.
    """
    answerDiscount = 0.2
    answerNoise = 0
    answerLivingReward = 0.4
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    """
        Prefer the close exit (+1), but avoiding the cliff (-10). Assuming there is no living reward, assume movement to be certain.
        works for discount 0.1/0.2/0.3 and noise 0.1/0.2/0.3 and reward 0.
    """
    answerDiscount = 0.2
    answerNoise = 0.1
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    """
        Prefer the close exit (+1), but avoiding the cliff (-10). Assuming there is no living reward, assume movement to be certain.
        works for discount 0.1/0.2/0.3 and noise 0.1/0.2/0.3 and reward 0.
    """
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0.9
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    """
        Prefer the distant exit (+10), avoiding the cliff (-10)
        I choose 0.9 discount factor as the higher the discount factor, the farther our rewards will propagate through time.
        0.1 as noise as lesser noise is preferrable and 0.6 as more reward is preferrable, but more living reward may make
        agent lazy and greedy, so I choose 0.6 for living reward
    """
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = 0.6
    return answerDiscount, answerNoise, answerLivingReward
   
def question3e():
    """
        Avoid both exits and the cliff (so an episode should never terminate)
        Works for discount 1 and noise 1 and reward 1.
    """
    answerDiscount = 1
    answerNoise = 1
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward

def question6():
    """
        Tried different variations for epsilon(0-1) and learning rate(0-1).Unable land at correct output.
        epsilon-greedy concepts, If high epsilon, though we learn we make bad decisions. If epsilon is too low,
        we don't explore much we don't learn much. so better way is to reduce epsilon over time and decreasing randomness
        leading to optimal learning.
    """
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
