import sys
import random

score = 0
score_percent = 100.00
total = 0

problem_states = {}

states_caps = {
        'AL':{'state':'Alabama',        'capital':'Montgomery'},
        'AK':{'state':'Alaska',         'capital':'Juneau'},
        'AZ':{'state':'Arizona',        'capital':'Phoenix'},
        'AR':{'state':'Arkansas',       'capital':'Little Rock'},
        'CA':{'state':'California',     'capital':'Sacramento'},
        'CO':{'state':'Colorado',       'capital':'Denver'},
        'CT':{'state':'Connecticut',    'capital':'Hartford'},
        'DE':{'state':'Deleware',       'capital':'Dover'},
        'FL':{'state':'Florida',        'capital':'Tallahassee'},
        'GA':{'state':'Georgia',        'capital':'Atlanta'},
        'HI':{'state':'Hawaii',         'capital':'Honolulu'},
        'ID':{'state':'Idaho',          'capital':'Boise'},
        'IL':{'state':'Illinois',       'capital':'Springfield'},
        'IN':{'state':'Indiana',        'capital':'Indianapolis'},
        'IA':{'state':'Iowa',           'capital':'Des Moines'},
        'KS':{'state':'Kansas',         'capital':'Topeka'},
        'KY':{'state':'Kentucky',       'capital':'Frankfort'},
        'LA':{'state':'Louisiana',      'capital':'Baton Rouge'},
        'ME':{'state':'Maine',          'capital':'Augusta'},
        'MD':{'state':'Maryland',       'capital':'Annapolis'},
        'MA':{'state':'Massachusetts',  'capital':'Boston'},
        'MI':{'state':'Michigan',       'capital':'Lansing'},
        'MN':{'state':'Minnesota',      'capital':'Saint Paul'},
        'MS':{'state':'Mississippi',    'capital':'Jackson'},
        'MO':{'state':'Missouri',       'capital':'Jefferson City'},
        'MT':{'state':'Montana',        'capital':'Helena'},
        'NE':{'state':'Nebraska',       'capital':'Lincoln'},
        'NV':{'state':'Nevada',         'capital':'Carson City'},
        'NH':{'state':'New Hampshire',  'capital':'Concord'},
        'NJ':{'state':'New Jersey',     'capital':'Trenton'},
        'NM':{'state':'New Mexico',     'capital':'Santa Fe'},
        'NY':{'state':'New York',       'capital':'Albany'},
        'NC':{'state':'North Carolina', 'capital':'Raleigh'},
        'ND':{'state':'North Dakota',   'capital':'Bismarck'},
        'OH':{'state':'Ohio',           'capital':'Columbus'},
        'OK':{'state':'Oklahoma',       'capital':'Oklahoma City'},
        'OR':{'state':'Oregon',         'capital':'Salem'},
        'PA':{'state':'Pennsylvania',   'capital':'Harrisburg'},
        'RI':{'state':'Rhode Island',   'capital':'Providence'},
        'SC':{'state':'South Carolina', 'capital':'Columbia'},
        'SD':{'state':'South Dakota',   'capital':'Pierre'},
        'TN':{'state':'Tennessee',      'capital':'Nashville'},
        'TX':{'state':'Texas',          'capital':'Austin'},
        'UT':{'state':'Utah',           'capital':'Salt Lake City'},
        'VT':{'state':'Vermont',        'capital':'Montpelier'},
        'VA':{'state':'Virginia',       'capital':'Richmond'},
        'WA':{'state':'Washington',     'capital':'Olympia'},
        'WV':{'state':'West Virginia',  'capital':'Charleston'},
        'WI':{'state':'Wisconsin',      'capital':'Madison'},
        'WY':{'state':'Wyoming',        'capital':'Cheyenne'},
    }

total_states = len(states_caps)

def add_problem_state(state_abbr):
    """
    Add any states you're having problems with here.
    """
    if state_abbr in problem_states:
        problem_states[state_abbr] += 1
    else:
        problem_states[state_abbr] = 1

def get_next_state():
    """
    Retrieves the next state from the master list.
    """
    k = random.sample(states_caps.keys(), 1)
    if len(k):
        s = states_caps[k[0]]['state']
        c = states_caps[k[0]]['capital']
        return [k[0], s, c]

def print_final_stats(total, score, problem_states):
    """
    Prints final statistics once we're done being tested.
    """
    score_percent = int((float(score) / float(total)) * 100)
    
    print '\n'
    print '***** FINAL RESULTS *****'
    print 'Total States:', total_states
    print 'Total Answered:', total
    print 'Total Correct:', score
    print '%1.2f%% Correct' % score_percent 
    print 'Problem States:'
    for key, value in sorted(problem_states.iteritems(), key=lambda (k,v): (v, k), reverse=True):
        print "\tState: {state}, Count: {num_wrong}".format(state = key, num_wrong = problem_states[key])
    
    if 0 <= score_percent <= 25:
        print 'Summary: Boy do you need practice.'
    elif 26 <= score_percent <= 50:
        print 'Summary: Pretty good, but keep practicing!'
    elif 51 <= score_percent <= 75:
        print 'Summary: With a little more practice, you\'ll do great!'
    elif 76 <= score_percent <= 90:
        print 'Summary: You\'re doing very well. Keep it up!'
    elif 91 <= score_percent <= 98:
        print 'Summary: So close. Don\'t give up now!'
    elif 98 <= score_percent <= 99:
        print 'Summary: Nearly perfect! Great work!'
    elif score_percent == 100:
        print 'Summary: Perfection. Outstanding.'
    
    print '\n'
    
    sys.exit(0)

while True:
    try:
        random_state_abbr, random_state, random_capital = get_next_state()
        total += 1
        
        print "What is the state capital of {state}?".format(state = random_state)
        capital_answer = raw_input()
        capital_answer = capital_answer.strip()
        
        if (capital_answer.upper() == random_capital.upper()):
            score += 1
            print "That is correct!"
            del states_caps[random_state_abbr]
        else:
            print "Wrong! The answer is: {answer}".format(answer = random_capital)
            add_problem_state(random_state_abbr)

    except ValueError:
        print_final_stats(total, score, problem_states)