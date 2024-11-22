# # Full Api based programme coming soon 
# import requests


# def random_product_freeApi():
#     Api_url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
#     response = requests.get(Api_url)
#     data = response.json()

#     if data["success"] and "data" in data:

#        product_data = data["data"]

#        item_quantity = product_data["data"][0]["id"]
#        product_title = product_data["data"][0]["title"]
#        return item_quantity, product_title
#     else :
#         raise Exception("Failed to fetch Data ")

# def main():
#     try:
#         item_quantity,product_title =random_product_freeApi()

#         print(f"\n\"Product_title\" : {product_title} , \n ID : {item_quantity}")
#     except Exception as e :
#         print(str(e))
# if __name__ == "__main__":
#     main()

    


        