INTRODUCTION:
PhasePhinder: An Open-Sourced App for Propagation-Based Phase Contrast in Lab XCT 
 
Phase contrast imaging (PCI) significantly enhances the visualization of internal structures in X-ray computed tomography (XCT) by exploiting variations in phase shifts rather than absorption contrast. However, achieving optimal phase contrast requires precise alignment and positioning of the detector and the source, which can be challenging in laboratory settings. To address this, PhasePhinder, an open-source application designed to simplify the propagation-based PCI setup in lab-based XCT systems was developed. 
 
PhasePhinder takes the optical magnification and source distance parameters from the ZEISS Xradia Versa XCT system and calculates the optimal region for placing the detector to maximize phase contribution. By automating these calculations, the application reduces the complexity and time required for setup, enabling users to achieve high-quality PCI more efficiently. 
 
The application was tested in various experiments to validate its accuracy, consistently identifying the optimal configuration, leading to significant improvements in image quality and cleaner segmentations. This tool not only facilitates easier implementation of PCI but also promotes wider adoption of advanced imaging techniques in lab-based XCT research.

   
Figure 1: Trendlines of Source-Sample-Detector distances for optimal propagation-based PCI in Versa XCT.  

INSTALLATION:

The PhasePhinder app (PhasePhinder.exe) should be downloaded with the “phasy_new.ico” and kept in the same folder. 
PhasePhinder.exe calls on phasy_new.ico as the applications icon, a friendly ghost named Phasy!

Once the application is installed the following display will appear. 

 
Figure 2: Front panel of PhasePhinder.exe

The user simply chooses the voltage range and the optical magnification they are using which triggers variables in the code and lets the application know which parameters to look up. 
The user then sets a number into “Source to sample distance (mm)” in millimeters and presses “Find phase region”. This will give the user the distance to place their detector for optimal PCI in the lab-based XCT. 
This front panel acts as an interactive look up table for the plots in Figure 1 which give the optimal region for propagation-based PCI. 

