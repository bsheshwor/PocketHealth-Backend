from django.urls import path
from django.urls.resolvers import URLPattern

from .views import PatientRegistration, PractitionerRegistration, UserLogin,PeriodViewSet,ContactPointViewSet,DeceasedViewSet,AddressViewSet,HumanNameViewSet,MaritalStatusViewSet,ContactViewSet,CommunicationViewSet,TelecomViewSet,LinkViewSet
from .views import OrganizationViewSet,OrganizationContactViewSet,HealthcareServiceViewSet,HealthcareCategoryViewSet,TypeViewSet,SpecialityViewSet,ServiceProvisionCodeViewSet,ProgramViewSet,ReferralMethodViewSet,availableTimeViewSet,notAvailableTimeViewSet,CareTeamViewSet,StatusCodeViewSet,ParticipantRoleViewSet, ParticipantViewSet,ReasonCodeViewSet,AnnotationViewSet,AuthorViewSet,LocationViewSet,StatusViewSet,OperationalStatusViewSet,ModeViewSet,TypesViewSet,PhysicalLocationTypeViewSet,PositionViewSet,HoursOfOperationViewSet
app_name = 'account'

urlpatterns = [
    path('patient_register/', PatientRegistration.as_view(), name='patient_register'),
    path('practitioner_register/', PractitionerRegistration.as_view(), name='practitioner_register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('period/', PeriodViewSet.as_view({'get': 'list', 'post':'create'}), name="create_period"),
    path('period/<int:pk>', PeriodViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='period'),
    path('contact_point/', ContactPointViewSet.as_view({'get': 'list', 'post':'create'}), name='contact_point'),
    path('contact_point/<int:pk>', ContactPointViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='contact-point'),
    path('deceased/', DeceasedViewSet.as_view({'get': 'list', 'post':'create'}), name='deceased'),
    path('deceased/<int:pk>', DeceasedViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='deceased-detail'),
    path('address/', AddressViewSet.as_view({'get': 'list', 'post':'create'}), name='address'),
    path('address/<int:pk>', AddressViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='address-detail'),
    path('human_name/', HumanNameViewSet.as_view({'get': 'list', 'post':'create'}), name='human_name'),
    path('human_name/<int:pk>', HumanNameViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='human_name-detail'),
    path('marital_status/', MaritalStatusViewSet.as_view({'get': 'list', 'post':'create'}), name='marital_status'),
    path('marital_status/<int:pk>', MaritalStatusViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='marital_status-detail'),
    path('contact/', ContactViewSet.as_view({'get': 'list', 'post':'create'}), name='contact'),
    path('contact/<int:pk>', ContactViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='contact-detail'),
    path('communication/', CommunicationViewSet.as_view({'get': 'list', 'post':'create'}), name='communication'),
    path('communication/<int:pk>', CommunicationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='communication-detail'),
    path('telecom/', TelecomViewSet.as_view({'get': 'list', 'post':'create'}), name='telecom'),
    path('telecom/<int:pk>', TelecomViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='telecom-detail'),
    path('link/', LinkViewSet.as_view({'get': 'list', 'post':'create'}), name='link'),
    path('link/<int:pk>', LinkViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='link-detail'),
    path('oraganization/', OrganizationViewSet.as_view({'get': 'list', 'post':'create'}), name='oraganization'),
    path('oraganization/<int:pk>', OrganizationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='oraganization-detail'),
    path('oraganization/contact/', OrganizationContactViewSet.as_view({'get': 'list', 'post':'create'}), name='oraganization_contact'),
    path('oraganization/contact/<int:pk>', OrganizationContactViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='oraganization-contact-detail'), 
    path('healthcareservice/', HealthcareServiceViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice'),
    path('healthcareservice/<int:pk>', HealthcareServiceViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-detail'),                                 
    path('healthcareservice/category/', HealthcareCategoryViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-category'),
    path('healthcareservice/category/<int:pk>', HealthcareCategoryViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-category-detail'),
    path('healthcareservice/type/', TypeViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-type'),
    path('healthcareservice/type/<int:pk>', TypeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-type-detail'),
    path('healthcareservice/speciality/', SpecialityViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-speciality'),
    path('healthcareservice/speciality/<int:pk>', SpecialityViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-speciality-detail'),
    path('healthcareservice/serviceprovisioncode/', ServiceProvisionCodeViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-serviceprovisioncode'),
    path('healthcareservice/serviceprovisioncode/<int:pk>', ServiceProvisionCodeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-serviceprovisioncode-detail'),
    path('healthcareservice/program/', ProgramViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-program'),
    path('healthcareservice/program/<int:pk>', ProgramViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-program-detail'),
    path('healthcareservice/referralmethod/', ReferralMethodViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-referralmethod'),
    path('healthcareservice/referralmethod/<int:pk>', ReferralMethodViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-referralmethod-detail'),
    path('healthcareservice/availabletime/', availableTimeViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-availabletime'),
    path('healthcareservice/availabletime/<int:pk>', availableTimeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-availabletime-detail'),
    path('healthcareservice/notavailabletime/', notAvailableTimeViewSet.as_view({'get': 'list', 'post':'create'}), name='healthcareservice-notavailabletime'),
    path('healthcareservice/notavailabletime/<int:pk>', notAvailableTimeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='healthcareservice-notavailabletime-detail'),
    path('careteam/', CareTeamViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam'),
    path('careteam/<int:pk>', CareTeamViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-detail'),
    path('careteam/statuscode/', StatusCodeViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-statuscode'),
    path('careteam/statuscode/<int:pk>', StatusCodeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-statuscode-detail'),
    path('careteam/participantrole/', ParticipantRoleViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-participantrole'),
    path('careteam/participantrole/<int:pk>', ParticipantRoleViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-participantrole-detail'), 
    path('careteam/participant/', ParticipantViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-participant'),
    path('careteam/participant/<int:pk>', ParticipantViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-participant-detail'), 
    path('careteam/reasoncode/', ReasonCodeViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-reasoncode'),
    path('careteam/reasoncode/<int:pk>', ReasonCodeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-reasoncode-detail'),                                 
    path('careteam/anotation/', AnnotationViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-anotation'),
    path('careteam/anotation/<int:pk>', AnnotationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-anotation-detail'),
    path('careteam/author/', AuthorViewSet.as_view({'get': 'list', 'post':'create'}), name='careteam-author'),
    path('careteam/author/<int:pk>', AuthorViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='careteam-author-detail'),
    path('location/', LocationViewSet.as_view({'get': 'list', 'post':'create'}), name='location'),
    path('location/<int:pk>', LocationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-detail'),
    path('location/status/', StatusViewSet.as_view({'get': 'list', 'post':'create'}), name='location-status'),
    path('location/status/<int:pk>', StatusViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-status-detail'),
    path('location/operationalstatus/', OperationalStatusViewSet.as_view({'get': 'list', 'post':'create'}), name='location-operationalstatus'),
    path('location/operationalstatus/<int:pk>', OperationalStatusViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-operationalstatus-detail'),
    path('location/mode/', ModeViewSet.as_view({'get': 'list', 'post':'create'}), name='location-mode'),
    path('location/mode/<int:pk>', ModeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-mode-detail'),
    path('location/types/', TypesViewSet.as_view({'get': 'list', 'post':'create'}), name='location-types'),
    path('location/types/<int:pk>', TypesViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-types-detail'),
    path('location/physicallocationtype/', PhysicalLocationTypeViewSet.as_view({'get': 'list', 'post':'create'}), name='location-physicallocationtype'),
    path('location/physicallocationtype/<int:pk>', PhysicalLocationTypeViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-physicallocationtype-detail'),
    path('location/position/', PositionViewSet.as_view({'get': 'list', 'post':'create'}), name='location-position'),
    path('location/position/<int:pk>', PositionViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-position-detail'),
    path('location/hoursofoperation/', HoursOfOperationViewSet.as_view({'get': 'list', 'post':'create'}), name='location-hoursofoperation'),
    path('location/hoursofoperation/<int:pk>', HoursOfOperationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='location-hoursofoperation-detail'),

]