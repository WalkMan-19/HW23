from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()

# {
#     "queries":[
#         {
#             "cmd": "filter",
#             "value": "POST"
#         },
#         {
#             "cmd": "sort",
#             "value": "asc"
#         },
#         {
#             "cmd": "map",
#             "value": "0"
#         },
#         {
#             "cmd": "unique",
#             "value": ""
#         },
#         {
#             "cmd": "limit",
#             "value": "4"
#         },
#         {
#             "cmd": "regex",
#             "value": "images/\\w+\\.png"
#         }
#     ]
# }
