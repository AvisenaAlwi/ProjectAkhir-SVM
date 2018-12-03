import numpy as np
import pandas as pd

sqrt = lambda x : x**(float(1/2))

def norm(data, dataTest):
	dataTestValue = ( dataTest - np.min(data) ) / ( np.max(data) - np.min(data) )
	return ( data - np.min(data) ) / ( np.max(data) - np.min(data) ) , np.clip( dataTestValue , 0, 1)

# NORMAL 1
# TIDAK -1

excel = pd.read_excel('Data.xlsx')
data = excel.values

x1 = data[:,0]
x2 = data[:,1]
y = np.array ( [ 1 if value == 'normal' else -1   for value in data[:,2] ] )
yiyj = np.array( [ [ y[i]*y[j] for j in range(0,len(y)) ] for i in range(0,len(y)) ] )

# Fungsi kernel polinomial ordo 2
# =(x*y + c)^2

def calculate_kernel(u,z) :
	""" Menghitung 1 Elemen untuk matrix kernel
	
	Arguments:
		u {numpy array} -- mengandung nilai u1 dan u2 => [1,1]
		z {numpy array} -- mengandung nilai z1 dan z1 => [1,-1]
	
	Returns:
		int -- integer skalar yang nantinya digunakan pada elemen matrix kernel
	"""

	return ( (u[0]*z[0]) + (u[1]*z[1]) + 1 ) ** 2

def kernel(x1,x2) :
	""" Mendapatkan matrix kernel dari fitur x1 dan x2
	rumus :
	K(x,xj)
	
	Arguments:
		x1 {numpy array} -- array fitur 1 pada semua baris data
		x2 {numpy array} -- array fitur 2 pada semua baris data
	
	Returns:
		numpy array 2 dimensi -- matrix kernel
	"""

	matrix_kernel = []
	banyak_data = len(x1)
	for i in range(0, banyak_data):
		row = []
		for j in range(0, banyak_data):
			row.append( calculate_kernel( [ x1[i], x2[i] ], [ x1[j], x2[j] ] ) )
		matrix_kernel.append(row)
	matrix_kernel = np.array(matrix_kernel)
	return matrix_kernel

def get_alpha(matrix_kernel, lamb, gama, C) :
	""" Mendapatkan nilai alpha (α)
	
	Arguments:
		matrix_kernel {numpy array 2 dimensi} -- matrix kernel dari fungsi kernel()
		lamb {number} -- bilngan skalar sembarang
		gama {number} -- 0 < ܓ < 2 / max[Dij]
		C {number} -- C > 1
	
	Returns:
		numpy array -- nilai alpha
	"""

	alpha = np.array([ 0 for i in range(0,len(matrix_kernel))])
	k_plus_lambda_squre = matrix_kernel + (lamb ** 2)
	Dij = k_plus_lambda_squre * yiyj
	last_alpha = np.array([])
	while True : # lakukan perulangan terus sampai konvergen
		last_alpha = np.copy(alpha)
		temp = []
		for i in range(0, len(alpha) ) :
			Ei = np.sum(Dij[:,i] * alpha[i])
			delta = min( max ( gama * (1-Ei) , -alpha[i] )  , C-alpha[i] )
			temp.append(delta + alpha[i])
		alpha = np.array(temp)

		# Jika sudah konvergen maka hentikan perulangan
		if np.allclose(alpha , last_alpha, rtol=1e-08, atol=1e-08) :
			break

	return alpha


def ld(matrix_kernel, alpha) :
	""" Hitung nilai Ld
	
	Arguments:
		matrix_kernel {numpy array 2 dimensi} -- matrix kernel
		alpha {[type]} -- [description]
	
	Returns:
		[type] -- [description]
	"""

	
	size = len(yiyj)
	z = alpha * yiyj * matrix_kernel
	return np.sum(alpha) + np.sum(z) / 2

def phi(x1, x2):
	""" Mengitung nilai phi ( ɸ )
	Misal kita pengen dapet nilai ɸ dari data ke 2, jadi kita 

	PPT Slide 23 atas

	Arguments:
		x1 {number} -- nilai fitur 1 pada baris tertentu
		x2 {number} -- nilai fitur 2 pada baris tertentu
	
	Returns:
		[type] -- [description]
	"""

	return np.array([ x1**2 , sqrt(2)*x1*x2, x2**2, sqrt(2)*x1, sqrt(2)*x2, 1 ])

def get_w(alpha):
	""" Menghitung nilai W
	PPT slide ke 23-24
	
	Arguments:
		alpha {numpy array 1 dimensi} -- nilai alpha masing masing data
	
	Returns:
		numpy array 1 dimensi -- w
	"""

	w = np.array([0,0,0,0,0,0])
	alpha = alpha * y
	for i in range(0, len(alpha)) :
		al = alpha[i]
		p = phi(x1[i], x2[i])
		z = p * al
		w = w + z
	return w

def get_b(w, xplus, xmin):
	""" Menghitung nilai B
	
	Arguments:
		w {numpy array 1 dimensi} -- nilai w
		xplus {numpy array} -- support vector dari salah satu data class  positif
		xmin {numpy array} -- support vector dari salah satu data class  positif
	
	Returns:
		number -- nilai B
	"""

	return -( np.sum(w*xplus) + np.sum(w*xmin) )/2


beratBadan = float(input('Berat Badan : '))
tinggiBadan = float(input('Tinggi Badan : '))

x1, beratBadan = norm(x1, beratBadan)
x2, tinggiBadan = norm(x2, tinggiBadan)

kernel = kernel(x1,x2)
alpha = get_alpha(kernel, 3, 0.1, 5 )
w = get_w(alpha)
b = get_b(w, phi(x1[1],x2[1]), phi(x1[3],x2[3]))
fx = np.sum(w * phi( beratBadan , tinggiBadan )) + b

print()
print("Termasuk : ", end="")
if (fx < 0):
	print('Tidak normal')
else : 
	print('Normal')