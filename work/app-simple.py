from python_graphql_client import GraphqlClient

def get_data(size):
    client = GraphqlClient(endpoint="https://axieinfinity.com/graphql-server-v2/graphql")
    query = """
        query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) 
        {  
            axies(
                auctionType: $auctionType, 
                criteria: $criteria, 
                from: $from, 
                sort: $sort, 
                size: $size, 
                owner: $owner) 
            {    
                total    
                results {      
                    ...AxieBrief      
                    __typename    
                }    
                __typename  
            }
        }
        fragment AxieBrief on Axie {  
            id  name  stage  class  breedCount  image  title  battleInfo 
            {    banned    __typename  }  
            auction {    currentPrice    currentPriceUSD    __typename  }  
            parts {    id    name    class    type    specialGenes    __typename  }  
            __typename
        }
    """
    variables = {
                    "from":0,
                    "size":size,
                    "sort":"Latest",
                    "auctionType":"Sale",
                    "owner":None,
                    "criteria":{
                        "region":None,
                        "parts":None,
                        "bodyShapes":None,
                        "classes":None,
                        "stages":None,
                        "numMystic":None,
                        "pureness":None,
                        "title":None,
                        "breedable":None,
                        "breedCount":None,
                        "hp":[],
                        "skill":[],
                        "speed":[],
                        "morale":[]
                    }
                }
    data = client.execute(query=query, variables=variables)
    return data

def get_data(size):
    client = GraphqlClient(endpoint="https://axieinfinity.com/graphql-server-v2/graphql")
    query = """
        query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) 
        {  
            axies(
                auctionType: $auctionType, 
                criteria: $criteria, 
                from: $from, 
                sort: $sort, 
                size: $size, 
                owner: $owner) 
            {    
                total    
                results {      
                    ...AxieBrief      
                    __typename    
                }    
                __typename  
            }
        }
        fragment AxieBrief on Axie {  
            id  name  stage  class  breedCount  image  title  battleInfo 
            {    banned    __typename  }  
            auction {    currentPrice    currentPriceUSD    __typename  }  
            parts {    id    name    class    type    specialGenes    __typename  }  
            __typename
        }
    """
    variables = {
                    "from":0,
                    "size":size,
                    "sort":"Latest",
                    "auctionType":"Sale",
                    "owner":None,
                    "criteria":{
                        "region":None,
                        "parts":None,
                        "bodyShapes":None,
                        "classes":None,
                        "stages":None,
                        "numMystic":None,
                        "pureness":None,
                        "title":None,
                        "breedable":None,
                        "breedCount":None,
                        "hp":[],
                        "skill":[],
                        "speed":[],
                        "morale":[]
                    }
                }
    data = client.execute(query=query, variables=variables)
    return data
def get_total():
    client = GraphqlClient(endpoint="https://axieinfinity.com/graphql-server-v2/graphql")
    query = """
        query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) 
        {  
            axies(
                auctionType: $auctionType, 
                criteria: $criteria, 
                from: $from, 
                sort: $sort, 
                size: $size, 
                owner: $owner) 
            {    
                total
            }
        }
    """
    variables = {
                    "from":0,
                    "size":1,
                    "sort":"Latest",
                    "auctionType":"Sale",
                    "owner":None,
                    "criteria":{
                        "region":None,
                        "parts":None,
                        "bodyShapes":None,
                        "classes":None,
                        "stages":None,
                        "numMystic":None,
                        "pureness":None,
                        "title":None,
                        "breedable":None,
                        "breedCount":None,
                        "hp":[],
                        "skill":[],
                        "speed":[],
                        "morale":[]
                    }
                }
    data = client.execute(query=query, variables=variables)
    return data['data']['axies']['total']

def show_whole(results):
    for f in results:
        print(f)
        print("")
        print("")
        print("")

def show_simple(results):
    for res in results:
        print(f"id={res['id']}"+
            f", name={res['name']}"+   
            f", stage={res['stage']}"+  
            f", class={res['class']}"+  
            f", breedCount={res['breedCount']}"+
            f", currentPriceUSD={res['auction']['currentPriceUSD']}"
        )

if __name__ == "__main__":
    result = get_data(1)
    total = result['data']['axies']['total']
    show_simple(result['data']['axies']['results'])

    while True:
        current_total = get_total()
        size = current_total - total
        if(size > 0):
            result = get_data(size)
            total = result['data']['axies']['total']
            print("")
            print(f"total count = {total}")
            show_simple(result['data']['axies']['results'])
            
        