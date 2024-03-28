Description:
This is to test pet endpoint of the pet store api. It covers basic positive cases on each endpoint under pet.

Test suite:
pet_api/tests/test_pet_api.py

Test data:
In each case, a new pet will be generated dynamically and added. After each case is done, the pet will be deleted at teardown step.

Test cases:
1. Test add a new pet with valid payload
2. Test get a pet info by id
3. Test update a pet data by post
4. Test delete a pet
5. Test get pets by status
6. Test update a pet data by form
7. Test upload image for a pet

How to run in github:
1. Click on the "Actions" tab
2. In the left sidebar, select "Pet Store Automation Test"
3. Click on the "Run workflow" dropdown button
4. Select the branch feature/Anna-CBATest
5. Click the "Run workflow" button
6. Monitor the workflow execution

How to run locally:
1. Clone the repo to your local
2. Run pip install -r requirements.txt to install python packages needed
3. Under cba_test, run
   pytest -sv pet_api/tests/test_pet_api.py

   or run this to generate a html report under report folder
   pytest -sv pet_api/tests/test_pet_api.py --html=./report/pet_api_test_report.html --self-contained-html