def binding_energy_calculator(A,Z): #All in MeV
    BE1 = 15.56*A - 17.23*(A**(2/3)) - 0.697*(Z**2)*(A**(-1/3)) - 23.285*((A-2*Z)**2)/A
    
    if (A-Z)%2 != 0 and Z%2 != 0:       #This if statement deals with the pairing term
        BE2 = BE1 + (12/(A**0.5))

    elif A%2 !=0:
        BE2 = BE1

    else: BE2 = BE1 - (12/(A**0.5))



    return Z*938.28 + (A-Z)*939.57 - BE2 #mass energy of the nucleus minus BE

#Lets use this to get an answer! 

m_sb = binding_energy_calculator(111,51)
m_sn = binding_energy_calculator(111,50)

q = m_sb - (m_sn + 0.511) #0.511 is mass of electron so this is Q value for beta decay

print("The Q value for this reaction is", q)