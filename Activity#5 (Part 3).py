# -*- coding: utf-8 -*-
"""
Created on Sat Mar 9 10:21:10 2024

@author: smgabriel
"""
import scipy as sp

unnormalized_posterior = likelihood_out * uniform_dist
plt.plot(mu, unnormalized_posterior)
plt.xlabel("$\mu$ in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()
