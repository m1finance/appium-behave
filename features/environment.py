import os
from time import sleep
from appium import webdriver


def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):
    if 'android' in feature.tags:
        app = os.path.join(os.path.dirname(__file__),
                           '../apps',
                           'app-develop-debug.apk')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app' : app,
                'appPackage': 'com.m1finance.android.dev',
                'appActivity': 'com.m1finance.android.auth.AuthActivity',
                'platformName' : 'Android',
                'automationName': 'espresso',
                'platformVersion' : '11.0',
                'deviceName' : 'Pixel_4_API_30',
                'allowTestPackages': True,
                'espressoBuildConfig': '{ "additionalAppDependencies": [ "com.google.android.material:material:1.0.0", "androidx.lifecycle:lifecycle-extensions:2.1.0" ] }'
                }
        )
    elif 'ios' in feature.tags:
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/',
                           'client.app')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "platformName": "iOS",
                "automationName": "XCUITest",
                "platformVersion": "14.4",
                "deviceName": "iPhone 11",
                "fullReset": True,
                
                "app": app
            })
        print(context.driver.session)

def after_feature(context, feature):
    sleep(1)
    # context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()