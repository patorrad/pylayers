from pylayers.simul.link import *
import pylayers.signal.waveform as wvf

# set the frequency range from 2.4GHz to 10GHz
fGHz = np.arange(2.4,10.,0.05)
# set the layout from its filename
L = Layout('defstr.lay')

# set the link
DL = DLink(L=L,fGHz=fGHz)
# set the b point position
DL.a = np.array([2,3,1.2])
DL.b = np.array([8,3.5,2.])
# evaluate the link in forcing re-calculation of
#
#   + signatures
#   + rays
#   + Tilded(*) Propagation Channel
#   + Transmission Channel H
#
# Diffraction : enabled
# Vectorization : enabled
#
DL.eval(cutoff=2, threshold=0.1, ra_vectorized=True, diffraction=True)
DL
DL.show()
plt.figure()
DL.H.show()
plt.title('Ray transfer funtion w.r.t frequency Modulus and Phase')
plt.show()
plt.figure()
DL.plt_cir()
plt.show()