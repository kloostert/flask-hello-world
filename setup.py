import setuptools

setuptools.setup(
    name='test_app',
    version='0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
        'https://github.com/flask-dashboard/Flask-MonitoringDashboard/tarball/monitor_tested_endpoints#egg=flask_monitoringdashboard'
    ],
    install_requires=(
        'flask_monitoringdashboard'
    )

)
