class LoginPagelocators(object):
    username_filed = 'Input_Email'
    password_filed = 'Input_Password'
    Sing_in_button = '/html/body/div/div/div/div/section/form/div[4]/button'


class LoginMicrosoft(object):
    username_filed = 'i0116'
    password_filed = 'i0118'
    next_btn = 'idSIButton9'
    # yes_btn ='idSIButton9'


class Homepagelocator(object):
    orders = '/html/body/app-root/div[1]/div/div[1]/left-nav/div/nav/a[2]/div/i'
    patients = '/html/body/app-root/div[1]/div/div[1]/left-nav/div/nav/a[3]/div'
    hcps = '/html/body/app-root/div[1]/div/div[1]/left-nav/div/nav/a[5]/div'


class L1orderlocator(object):
    order_details_btn = '/html/body/app-root/div[1]/div/div[2]/div[2]/app-orders/order-list/div/div/div[1]/div[2]/button'
    first_order = '//*[@id="igx-grid-0"]/div[2]/igx-display-container/igx-grid-row[1]/igx-display-container/igx-grid-cell[1]'
    close_btn = '//*[@id="orderDetailsModal"]/div/div/div[3]/button[2]'


class L1helthcarelocator(object):
    health_care_provider = 'igx-grid-15'
    health_care_provider_btn = '/html/body/app-root/div[1]/div/div[2]/div[2]/healthcare-providers/hcp-list/div/div/div/div/div[1]/div[2]/button'


class L1patients(object):
    first_patient = '//*[@id="igx-grid-0"]/div[2]/igx-display-container/igx-grid-row[1]/igx-display-container/igx-grid-cell[1]'
    patient_details_btn = '/html/body/app-root/div[1]/div/div[2]/div[2]/ng-component/div[1]/div/div/div/div[1]/div[2]/button'
    order_btn = '.btn:nth-child(3) > .d-flex'
    new_order = '.d-print-none > .col > span > .btn'
    enter_mx_btn = '//*[@id="orderModal"]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/mx-list[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/button[1]'
    daily_quantity = '.align-middle > .form-control'
    maximum_thc = 'tr:nth-child(3) .form-control'
    period_of_use = 'tr:nth-child(4) .form-control'

    # Next button
    # MEDICAL AUTHORIZATION form
    next_btn = '//*[@id="orderModal"]/div/div/div[4]/span/button[1]'

    # select a health care provider
    health_care_provider = '//*[@id="igx-grid-9"]/div[2]/igx-display-container/igx-grid-row[3]/igx-display-container/igx-grid-cell[1]'

    # health care provider button
    health_care_provider_btn ='//*[@id="orderModal"]/div/div/div[3]/div/div/div[2]/div[3]/hcp-list/div/div/div/div/div[1]/div[2]/button'

    new_order_next_btn ='.fa-arrow-right'

    # common issues
    common_issues = '/html/body/app-root/div[1]/div/div[2]/div[2]/ng-component/div[2]/div/div/div[3]/div/div/div[2]/div[5]/hi-list/div/div/div[2]/igx-grid/div[2]/igx-display-container/igx-grid-row[3]/igx-display-container/igx-grid-cell'
    # create MX button
    create_mx_btn ='.btn-success'

    close_new_order_btn ='.btn-danger > span'