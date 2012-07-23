# monte carlo robot localization program
# homework assignment for udacity AI course

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

def uniformDistribution():
  p = []
  for i in range(len(colors)):
    p.append([])
    for j in range(len(colors[i])):
        p[i].append(1./len(colors[i]))

  return p
        
def sense(p, Z):
  q= []
  for i in range(len(p)):
    q.append([])
    for j in range(len(p[i])):
      hit = (Z == colors[i][j])
      q[i].append( p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
        
  return normalize(q)

def normalize(q):
  s = 0
  for i in range(len(q)):
    s += sum(q[i])

  for i in range(len(q)):
    for j in range(len(q[i])):
      q[i][j] = q[i][j] / s
  
  return q

def move(p, U):
  q = []
  
  for i in range(len(p)):
    q.append([])
    for j in range(len(p[i])):
      ii = (i-U[0]) % len(p)
      jj = (j-U[1]) % len(p[i])
      s = p_move * p[ii][jj]
      s += (1-p_move) * p[i][j]
      q[i].append(s)
  return q

p = uniformDistribution()

for i in range(len(measurements)):
  #print '\nmove:'
  p = move(p, motions[i])
  #show(p)
  #print '\nsense:'
  p = sense(p, measurements[i])
  #show(p)

#print '\n'
#Your probability array must be printed 
#with the following code.

show(p)
