# Imports
import numpy as np
import matplotlib.pyplot as plt
import math

def TrigCircle(angulo):
  # Plotting the Circle
  x = np.arange(0, 2*np.pi ,0.01)
  y = np.sin(x)
  z = np.cos(x)
  plt.axis("equal")
  plt.grid()
  plt.xlim(-2, 2)
  plt.ylim(-2, 2)
  plt.plot(y, z, 'k', label='Unit Circle')

  # Plotting the hip line
  x1, y1 = 0, 0
  x2 = np.cos(np.radians(angulo))
  y2 = np.sin(np.radians(angulo))
  plt.plot([x1, x2], [y1, y2], 'r', label=f'{angulo} degree angle')

  # Plotting sine line
  plt.plot([x2, x2], [y2, 0], 'g', label=f'Sine: {y2:.3f}')

  # Plotting cosine line
  plt.plot([0, x2], [y2, y2], 'b', label=f'Cosine: {x2:.3f}')

  # Calculating the tangent
  tan = (np.sin(np.radians(angulo))/np.cos(np.radians(angulo)))

  # Plotting the secant line
  sec = 1/x2
  plt.plot([0, sec], [0, 0], 'purple', label=f'Secant: {sec:.3f}')

  # Calculating the cotangent line
  cot = 1/tan

  # Plotting the cossecant line
  csc = 1/y2
  plt.plot([0, 0], [0, csc], 'orange', label=f'Cossecant: {csc:.3f}')

  # Plotting cotangent line
  plt.plot([0, x2], [csc, y2], 'g--', label=f'Cotangent: {cot:.3f}')

  # Plotting tangent line
  plt.plot([x2, sec], [y2, 0], 'b--', label=f'Tangent: {tan:.3f}')

  if x2 > 0:
    plt.legend(loc='lower left')
  elif x2 < 0:
    plt.legend(loc='lower right')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()

TrigCircle(42)
