import numpy as np
""" Set of wave modules for initializing and
    driving the wavemaker field, that will be
    fed in and constrasted with field data. """

class Linear2D:
    def __init__(self,amplitude,omega,k,depth,rho_0,rho_1):
        self.A = amplitude
        self.omega = omega
        self.k = k
        self.h = depth
        self.rho_0 = rho_0      # density of water
        self.rho_1 = rho_1      # density of air

    def height(self,x,t):
        """ Gives a linearized solution for the air-water interface to the 
            potential flow model in two dimensions (x,y,z=eta) for finite depth."""
        eta = self.A*np.exp(1j*(self.k*x - self.omega*t))
        return np.real(eta)

    def pressure(self,x,t,z):
        """ Gives linearized pressured with P_atm = 0 """
        g = (0.0,0.0,-9.81)
        p = self.rho_0*(-g[2])*self.A* np.cosh(self.k*(z+self.h))/np.cosh(self.k*self.h) * np.exp(1j*(self.k*x - self.omega*t))
        return np.real(p)

    def velocity_u(self,x,t,z):
        """ Defines a linearized solution to the potential flow
            model in two dimensions (x,y,z) for finite depth,
            as well as, deep and shllow water limits."""
        g = (0.0,0.0,-9.81)                          # gravity

        # Finite Depth (0 < kh < infty)
        u = (-g[2]*self.k*self.A / self.omega) * np.cosh(self.k*(z+self.h))/np.cosh(self.k*self.h) * np.exp(1j*(self.k*x - self.omega*t))  

        # Deep water (kh >> 1)
        # ... TODO
                 
        # Shallow water (kh << 1)
        # ... TODO

        return np.real(u)


    def velocity_v(self,x,t,z):
        v = 0.0
        return v

    def velocity_w(self,x,t,z):
        """ Gives a linearized solution velocity in x-dir to the potential flow
            model in two dimensions (x,y,z) for finite depth, as well as, deep
            and shallow water limits."""
        g = (0.0,0.0,-9.81)                          # gravity
        
        # Finite Depth (0 < kh < infty)                                                                                                                                      
        w = -1j * (-g[2]*self.k*self.A/self.omega) * np.sinh(self.k*(z+self.h))/np.cosh(self.k*self.h) * np.exp(1j*(self.k*x - self.omega*t))

        # Deep Water (kh >> 1)
        # ... TODO

        # Shallow Water
        # ... TODO

        return np.real(w)


class WaveGroup:
    """ Class that defines a nearly monochromatic
        wave train/group of waves of same amplitude."""

    def __init__(self,amplitude,omega,k,depth,rho_0,rho_1):
        self.A = amplitude
        self.omega = omega
        self.k = k
        self.h = depth
        self.rho_0 = rho_0      # density of water                                      
        self.rho_1 = rho_1      # density of air  

    def height(self,x,t):
        N = 2
        theta =  self.k*x - self.omega*t
        dtheta = 0.1*theta
        eta = self.A*np.cos(theta)

        for i in range(N):
            eta = eta + self.A*np.cos(theta+(i+1)*dtheta) + self.A*np.cos(theta-(i+1)*dtheta)

        return eta


    def velocity_u(self,x,t,z):
        u = 0.0
        return u
        # NOTE: you can implement based on linearized ideal flow

    def velocity_v(self,x,t,z):
        v = 0.0
        return v
        # NOTE: you can implement based on linearized ideal flow   


    def velocity_w(self,x,t,z):
        w = 0.0
        return w
        # NOTE: you can implement based on linearized ideal flow   

    def pressure(self,x,t,z):
        p = 0.0    # P_atm
        return p
        # NOTE: also implement on ideal flow via linearized Bernoulli eqn.


class Solitary:
    def __init__(self,amplitude,omega,k,depth,rho_0,rho_1):
        self.A = amplitude
        self.omega = omega
        self.k = k
        self.h = depth
        self.rho_0 = rho_0      # density of water
        self.rho_1 = rho_1      # density of air         
        self.sigma = 4.0        # std. dev.

    def height(self,x,t):
        eta = self.A/np.cosh((self.k*x - self.omega*t)**2 / self.sigma**2)
        return eta

    def pressure(self,x,t,z):
        p = 0.0       # P_atm
        return
        # NOTE: define via Bernoulli eqn.

    def velocity_u(self,x,t,z):
        u = 0.0
        return u
        # NOTE: base it on linearized ideal fluid flow

    def velocity_v(self,x,t,z):
        v = 0.0
        return v
        # NOTE: base it on linearized ideal fluid flow
    
    def velocity_w(self,x,t,z):
        w = 0.0
        return w
        # NOTE: base it on ideal fluid flow
