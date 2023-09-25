def SLEbeforeSafeguard(AssetValue, EfbeforeSafeguard):
    return (AssetValue * EfbeforeSafeguard) / 100

def ALEbeforeSafeguard(SLE_before_Safeguard, ARO):
    return SLE_before_Safeguard * ARO

def SLEafterSafeguard(AssetValue, EfafterSafeguard):
    return (AssetValue * EfafterSafeguard) / 100

def ALEafterSafeguard(SLE_after_Safeguard, ARO):
    return SLE_after_Safeguard * ARO

AssetValue = float(input("Enter Asset Value: "))
EfbeforeSafeguard = float(input("Enter EF after Safeguard Value: "))
ARO = float(input("Enter ARO Value: "))
EfafterSafeguard = float(input("Enter EF after Safeguard Value: "))
Cost_of_Safegurad = float(input("Enter Cost of Safeguard Value: "))

SLE_before_Safeguard = SLEbeforeSafeguard(AssetValue, EfbeforeSafeguard)
ALE_before_Safeguard = ALEbeforeSafeguard(SLE_before_Safeguard,ARO)

SLE_after_Safeguard= SLEafterSafeguard(AssetValue, EfafterSafeguard)
ALE_after_Safeguard = ALEbeforeSafeguard(SLE_after_Safeguard,ARO)

ValueofSafeguard = ALE_before_Safeguard - ALE_after_Safeguard - Cost_of_Safegurad

if ValueofSafeguard > 0:
    print("Approved")
else:
    print("Rejected")
