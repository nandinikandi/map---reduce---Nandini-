import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 8) :
        Title,	Distributor,	ReleaseDate,	DomesticSales,	InternationalSales,	WorldSales,	MovieRuntime,	License = dataList 
        print (Distributor,"\t", Title)