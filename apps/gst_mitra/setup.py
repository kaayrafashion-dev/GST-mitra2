from setuptools import find_packages, setup

setup(
    name="gst_mitra",
    version="0.1.0",
    description="GST Mitra extensions for Frappe and ERPNext",
    author="GST Mitra",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
