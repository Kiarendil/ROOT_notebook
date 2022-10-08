import ROOT
from math import sqrt

# __ __ __ __ PDG TABLE 2018 __ __ __ __

PDG_MUON_MASS    =   0.1056583745
PDG_PION_MASS    =   0.13957061
PDG_PIOZ_MASS    =   0.1349770
PDG_KAON_MASS    =   0.493677
PDG_PROTON_MASS  =   0.9382720813
PDG_KSHORT_MASS  =   0.497611
PDG_KSHORT_DM    =   0.000013
PDG_KSHORT_TIME  =   0.8954 * 0.0000000001
PDG_KS_MASS      =   PDG_KSHORT_MASS
PDG_LAMBDA_MASS  =   1.115683 
PDG_LAMBDA_DM    =   0.000006 
PDG_LAMBDA_TIME  =   2.632 * 0.0000000001
PDG_SIGMA0_MASS  =   1.192642 
PDG_XImunus_MASS =   1.32171 
PDG_XImunus_DM   =   0.00007 
PDG_XImunus_TIME =   1.639 * 0.0000000001
PDG_OMmunus_MASS =   1.67245 
PDG_OMmunus_DM   =   0.00029 
PDG_OMmunus_TIME =   0.821 * 0.0000000001
PDG_DPM_MASS     =   1.86965 
PDG_DPM_DM       =   0.00005 
PDG_DPM_TIME     =   1.040 * 0.000000000001 
PDG_DZ_MASS      =   1.86483 
PDG_DZ_DM        =   0.00005 
PDG_DZ_TIME      =   0.4101 * 0.000000000001 
PDG_DS_MASS      =   1.96834 
PDG_DS_DM        =   0.00007 
PDG_DS_TIME      =   0.504 * 0.000000000001 
PDG_LAMCZ_MASS   =   2.28646 
PDG_LAMCZ_DM     =   0.00031 
PDG_LAMCZ_TIME   =   2.00 * 0.0000000000001
PDG_XICZ_MASS    =   2.47087 
PDG_XICZ_DM      =   0.00031 
PDG_XICZ_TIME    =   1.12 * 0.0000000000001
PDG_XICP_MASS    =   2.46787 
PDG_XICP_DM      =   0.00030 
PDG_XICP_TIME    =   4.42 * 0.0000000000001
PDG_KSTARZ_MASS  =   0.89555
PDG_KSTARZ_GAMMA =   0.0473 
PDG_KSTARP_MASS  =   0.89176
PDG_KSTARP_GAMMA =   0.0503 
PDG_PHI_MASS     =   1.019461
PDG_PHI_GAMMA    =   0.004249
PDG_JPSI_MASS    =   3.096900
PDG_PSI2S_MASS   =   3.686097
PDG_X3872_MASS   =   3.87169
PDG_BU_MASS      =   5.27932
PDG_BU_TIME      =   1.638 * 0.000000000001
PDG_B0_MASS      =   5.27963
PDG_B0_TIME      =   1.520 * 0.000000000001
PDG_BS_MASS      =   5.36689
PDG_BS_TIME      =   1.509 * 0.000000000001
PDG_BC_MASS      =   6.2749
PDG_BC_TIME      =   0.507 * 0.000000000001
PDG_LB_MASS      =   5.61960
PDG_LB_TIME      =   1.470 * 0.000000000001
PDG_XIBZ_MASS    =   5.7919
PDG_XIBZ_TIME    =   1.479 * 0.000000000001
PDG_XIBM_MASS    =   5.7970
PDG_XIBM_TIME    =   1.571 * 0.000000000001
PDG_OMBM_MASS    =   6.0461
PDG_OMBM_TIME    =   1.64 * 0.000000000001
PDG_C            =   29979245800. # in cm/c
#
# __ __ __ __ __ __ __ __ GENERAL STUFF __ __ __ __ __ __ __ __
#
SAMEEVENT            = ROOT.RooRealVar('SAMEEVENT'      , 'SAMEEVENT', -0.5, 1.5)
Ncands               = ROOT.RooRealVar('Ncands'         , 'Ncands'   , -0.1, 1000)
run                  = ROOT.RooRealVar('run'            ,  'run'     , 100000, 370000)
event                = ROOT.RooRealVar('event'          ,  'event'   , 0, 10000000000)
lumi                 = ROOT.RooRealVar('lumi'           ,  'lumi'    , 0, 4000)

#
# __ __ __ __ __ __ __ __ PSI VARS __ __ __ __ __ __ __ __
#

JPSI_mass_Cmumu       = ROOT.RooRealVar('JPSI_mass_Cmumu', 'M(#mu^{+} #mu^{#minus}) [GeV]', 2.9, 4             )
JPSI_pt_Cmumu         = ROOT.RooRealVar('JPSI_pt_Cmumu'  , 'p_{T}(J/#psi) [GeV]'        , 0  , 180             )
JPSI_pvdistsignif2_Cmumu = ROOT.RooRealVar('JPSI_pvdistsignif2_Cmumu', '(J/#psi)_{pvdistsign}', 0, 800         )
JPSI_vtxprob_Cmumu       = ROOT.RooRealVar('JPSI_vtxprob_Cmumu', 'J/#psi_{vtxprob}'            , 0  , 1        )

MU_pt               = ROOT.RooRealVar('MU_pt'          , 'p_{T}(#mu^{+}) [GeV]'       , 0, 120              )


#
# __ __ __ __ __ __ __ __ B-MESON VARS __ __ __ __ __ __ __ __
#

K1_pt              = ROOT.RooRealVar('K1_pt'        , 'p_{T}(K^{+}) [GeV]', 0 , 500                )
K1_pt_CV           = ROOT.RooRealVar('K1_pt_CV'     , 'p_{T}(K^{+}) [GeV]', 0 , 500                )
K1_eta             = ROOT.RooRealVar('K1_eta'       , '#eta(K^{+})'                , -3, 3                 )
K1_ips             = ROOT.RooRealVar('K1_ips'       , '(K^{+}_{ips})'              , 0 , 1000              )

B_mass_Cjp           = ROOT.RooRealVar('B_mass_Cjp'     , 'M(J/#psiK^{+}) [GeV]' , 5.1, 5.6           )
B_pt_Cjp             = ROOT.RooRealVar('B_pt_Cjp'           , 'p_{T}(B) [GeV]'     , 0, 500                  )
B_pvdist_Cjp         = ROOT.RooRealVar('B_pvdist_Cjp'       , '(B, PV)_{dist} [cm]', 0, 5000                  )
B_pvdistsignif2_Cjp  = ROOT.RooRealVar('B_pvdistsignif2_Cjp', '(B}, PV)_{detsign}'  , 0, 5000                 )
B_vtxprob_Cjp        = ROOT.RooRealVar('B_vtxprob_Cjp'      , '(B)_{vtxprob}'      , 0, 1                    )

B_pvcos2_Cjp         = ROOT.RooRealVar('B_pvcos2_Cjp'  , 'cos(B, PV)'                , -1, 1)

# 
# __ __ __ __ __ __ __ __ PHI VARS __ __ __ __ __ __ __ __
#
C_Phi_mass_Cmumu     = ROOT.RooRealVar('C_Phi_mass_Cmumu', 'M(#mu^{+} #mu^{#minus}) [GeV]', 0.9, 1.1         )
C_Phi_pt_Cmumu       = ROOT.RooRealVar('C_Phi_pt_Cmumu'  , 'p_{T}(#phi) [GeV]'        , 0  , 200             )
C_Phi_pvdistsignif2_Cmumu = ROOT.RooRealVar('C_Phi_pvdistsignif2_Cmumu', '(#phi)_{pvdistsign}', 0, 800       )
C_Phi_Prob_Cmumu     = ROOT.RooRealVar('C_Phi_Prob_Cmumu', '#phi_{vtxprob}'            , 0  , 1              )

MU1_pt               = ROOT.RooRealVar('MU1_pt'          , 'p_{T}(#mu^{+}) [GeV]'       , 0, 60              )
MU2_pt               = ROOT.RooRealVar('MU2_pt'          , 'p_{T}(#mu^{-}) [GeV]'       , 0, 60              )
MU1_ips              = ROOT.RooRealVar('MU1_ips'         , '(#mu^{+}_{ips})'            , 0 , 1000           )
MU2_ips              = ROOT.RooRealVar('MU2_ips'         , '(#mu^{-}_{ips})'            , 0 , 1000           )


#
# __ __ __ __ __ __ __ __ LAMBDA VARS __ __ __ __ __ __ __ __
#
LA_mass              = ROOT.RooRealVar('LA_mass'         , 'M(#Lambda) [GeV]'           , 1.08, 1.17         )
LA_pt                = ROOT.RooRealVar('LA_pt'           , 'p_{T}(#Lambda) [GeV]'       , 0, 60              )
LA_eta               = ROOT.RooRealVar('LA_eta'          ,  '#eta(#Lambda)'             , -3  , 3            )
LA_XIdist            = ROOT.RooRealVar('LA_XIdist'       , '(#Lambda, #Xi)_{dist} [cm]' , 0, 350             )
LA_XIdistsignif2     = ROOT.RooRealVar('LA_XIdistsignif2', '(#Lambda, #Xi)_{detsign}'   , 0, 1000            )
LA_XIdistsignif3     = ROOT.RooRealVar('LA_XIdistsignif3', '(#Lambda, #Xi)_{detsign3}'  , 0, 1000            )
LA_XBdistsignif2     = ROOT.RooRealVar('LA_XBdistsignif2', '(#Lambda, #Xi_{b})_{detsign}', 0, 30000          )
LA_XBdistsignif3     = ROOT.RooRealVar('LA_XBdistsignif3', '(#Lambda, #Xi_{b})_{detsign3}', 0, 30000         )

LA_vtxp              = ROOT.RooRealVar('LA_vtxp'         , '#Lambda_{vtxprob}'          , 0, 1               )

LA_pr_pt             = ROOT.RooRealVar('LA_pr_pt'        , 'p_{T}(p_{#Lambda}) [GeV]' , 0, 60                )
LA_pr_charg          = ROOT.RooRealVar('LA_pr_charg'     , 'q(#pi_{#Lambda}})'          , -1, 1              )
#
# __ __ __ __ __ __ __ __ REFLECTION ETC VARS __ __ __ __ __ __ __ __
#              
KS_mas1              = ROOT.RooRealVar('KS_mas1'        , 'M(#pi^{#pm} #pi^{#mp}) [GeV]'       , 0  , 0.65   )
B0_mass              = ROOT.RooRealVar('B0_mass'        , 'M(J/#psi #pi^{#pm} #pi^{#mp}) [GeV]', 3  , 20     )
XI_lamk_mass         = ROOT.RooRealVar('XI_lamk_mass'   , 'M(#Lambda #K^{#minus}) [GeV]'       , 1.2, 3.3    )
OmegaB_mass          = ROOT.RooRealVar('OmegaB_mass'    , 'M(J/#psi #Lambda #K^{#minus}) [GeV]', 5  , 20     )

Jpsi_LAM_mass        = ROOT.RooRealVar('Jpsi_LAM_mass'  , 'M(J/#psi #Lambda) [GeV]'            , 4.1, 5.6    )
Jpsi_ka_mass         = ROOT.RooRealVar('Jpsi_ka_mass'   , 'M(J/#psi K^{#minus}) [GeV]'         , 3.1, 4.8    )
LAM_ka_mass          = ROOT.RooRealVar('LAM_ka_mass'    , 'M(#Lambda K^{#minus}) [GeV]'         , 1.5, 3     )
#
# __ __ __ __ __ __ __ __ PION from B VARS __ __ __ __ __ __ __ __
#                    
B_pi_pt              = ROOT.RooRealVar('B_pi_pt'        , 'p_{T}(#pi^{#minus}) [GeV]', 0 , 80                )
B_pi_pt_CV           = ROOT.RooRealVar('B_pi_pt_CV'     , 'p_{T}(#pi^{#minus}) [GeV]', 0 , 80                )
B_pi_eta             = ROOT.RooRealVar('B_pi_eta'       , '#eta(#pi)'                , -3, 3                 )
B_pi_ips             = ROOT.RooRealVar('B_pi_ips'       , '(#pi_{ips})'              , 0 , 1000              )
B_pi_HPT             = ROOT.RooRealVar('B_pi_HPT'       , 'B_pi_HPT'                 , 0 , 10                )
#
# __ __ __ __ __ __ __ __ KAON from B VARS __ __ __ __ __ __ __ __
#                    
B_ka_pt              = ROOT.RooRealVar('B_ka_pt'        , 'p_{T}(K^{#minus}) [GeV]', 0 , 80                  )
B_ka_pt_CV           = ROOT.RooRealVar('B_ka_pt_CV'     , 'p_{T}(K^{#minus}) [GeV]', 0 , 80                  )
B_ka_eta             = ROOT.RooRealVar('B_ka_eta'       ,  '#eta(K)'                 , -3, 3                 )
B_ka_ips             = ROOT.RooRealVar('B_ka_ips'       , '(K_{ips})'                , 0 , 1000              )
B_ka_HPT             = ROOT.RooRealVar('B_ka_HPT'       , 'B_ka_HPT'                 , 0 , 10                )
#
# __ __ __ __ __ __ __ __ XI VARS __ __ __ __ __ __ __ __
#                     
XI_mass_old          = ROOT.RooRealVar('XI_mass_old'     , 'M(#Lambda #pi^{#minus}) [GeV]', 1.25, 1.4        )
XI_mass_CV           = ROOT.RooRealVar('XI_mass_CV'      , 'M(#Lambda #pi^{#minus}) [GeV]', 1.2 , 1.45       )
XI_mass              = ROOT.RooRealVar('XI_mass'         , 'M(#Lambda #pi^{#minus}) [GeV]', 1.2 , 1.45       )
XI_pt                = ROOT.RooRealVar('XI_pt'           , 'p_{T}(#Xi) [GeV]'           , 0   , 80           )
XI_pt_CV             = ROOT.RooRealVar('XI_pt_CV'        , 'p_{T}(#Xi) [GeV]'           , 0   , 80           )
XI_eta               = ROOT.RooRealVar('XI_eta'          ,  '#eta(#Xi)'                   , -3  , 3          )
XI_vtxp              = ROOT.RooRealVar('XI_vtxp'         , '#Xi_{vtxprob}'              , 0, 1               )
XI_XIBdist           = ROOT.RooRealVar('XI_XIBdist'      , '(#Xi, #Xi_{b})_{dist} [cm]'   , 0   , 500        )
XI_pvdistxy          = ROOT.RooRealVar('XI_pvdistxy'      , '(#Xi, PV)_{distxy} [cm]'   , 0   , 500          )
XI_XBdistsignif2     = ROOT.RooRealVar('XI_XBdistsignif2', '(#Xi, #Xi_{b})_{detsign}'     , 0   , 5000       )
XI_XBdistsignif3     = ROOT.RooRealVar('XI_XBdistsignif3', '(#Xi, #Xi_{b})_{detsign3}'    , 0   , 5000       )
XI_pvdistsignif2     = ROOT.RooRealVar('XI_pvdistsignif2', '(#Xi, PV)_{detsign}'          , 0   , 5000       )

                     
Xi_Xic_detsign       = ROOT.RooRealVar('XI_Cdistsignif2' , '(#Xi, #Xi_{c})_{detsign}'  , 0, 5000             )
Xi_Xic_detsign3      = ROOT.RooRealVar('XI_Cdistsignif3' , '(#Xi, #Xi_{c})_{detsign3}' , 0, 5000             )
                     
XI_pi_HPT            = ROOT.RooRealVar('XI_pi_HPT'  , 'XI_pi_HPT'                  , 0 , 10                  )
XI_pi_charg          = ROOT.RooRealVar('XI_pi_charg', 'q(#pi_{#Xi})'               , -1, 1                   )
XI_pi_ips            = ROOT.RooRealVar('XI_pi_ips'  , 'IPS(#pi_{#Xi})'               , 0 , 300               )
XI_pi_pt             = ROOT.RooRealVar('XI_pi_pt'   , 'p_{T}(#pi^{#minus}) [GeV]', 0 , 80                    )
XI_pi_pt_CV          = ROOT.RooRealVar('XI_pi_pt_CV', 'p_{T}(#pi^{#minus}) [GeV]', 0 , 80                    )
XI_pi_eta            = ROOT.RooRealVar('XI_pi_eta'  , '#eta(#pi_{#Xi})'            , -3, 3                   )
#
# __ __ __ __ __ __ __ __ D_S VARS __ __ __ __ __ __ __ __
#
C_mass_old           = ROOT.RooRealVar('C_mass_old'     , 'M(#phi #pi^{+}) [GeV]'  , 1.75, 2.15              )
C_pt                 = ROOT.RooRealVar('C_pt'           , 'p_{T}(D_{s}) [GeV]'     , 0, 80                   )
C_pvdist             = ROOT.RooRealVar('C_pvdist'       , '(D_{s}, PV)_{dist} [cm]', 0, 500                  )
C_pvdistsignif2      = ROOT.RooRealVar('C_pvdistsignif2', '(D_{s}, PV)_{detsign}'  , 0, 5000                 )
C_pvdistsignif3      = ROOT.RooRealVar('C_pvdistsignif3', '(D_{s}, PV)_{detsign3}' , 0, 5000                 )
C_vtxprob            = ROOT.RooRealVar('C_vtxprob'      , '(D_{s})_{vtxprob}'      , 0, 1                    )
C_mass_old_c0        = ROOT.RooRealVar('C_mass_old_c0'  , 'M(#phi #pi^{+}) [GeV]'  , 1.75, 2.15              )

C_pi_HPT             = ROOT.RooRealVar('C_pi_HPT'  , 'C_pi_HPT'                    , 0 , 10                  )
C_pi_charg           = ROOT.RooRealVar('C_pi_charg', 'q(#pi_{D_{s}})'              , -1, 1                   )
C_pi_ips             = ROOT.RooRealVar('C_pi_ips'  , 'IPS(#pi_{D_{s}})'            , 0 , 300                 )
C_pi_pt              = ROOT.RooRealVar('C_pi_pt'   , 'p_{T}(#pi_{D_{s}}) [GeV]'    , 0 , 80                  )
C_pi_pt_CV           = ROOT.RooRealVar('C_pi_pt_CV', 'p_{T}(#pi_{D_{s}}) [GeV]'    , 0 , 80                  )
C_pi_eta             = ROOT.RooRealVar('C_pi_eta'  , '#eta(#pi_{D_{s}})'           , -3, 3                   )


# __ __ __ __ __ __ __ __ LAMBDA_C VARS __ __ __ __ __ __ __ __
#                     
LamC_m               = ROOT.RooRealVar('C_mass_old'    , 'M(#Lambda #pi^{+}) [GeV]', 2.24, 2.32)
LamC_pt              = ROOT.RooRealVar('C_pt'          , 'p_{T}(#Xi) [GeV]'      , 0, 80)
LamC_pv_dist         = ROOT.RooRealVar('C_pvdist'     , '(#Xi, #Xi_{b})_{dist} [cm]' , 0, 500)
LamC_pv_detsign      = ROOT.RooRealVar('C_pvdistsignif2', '(#Xi, #Xi_{b})_{detsign}'  , 0, 5000)
LamC_pv_detsign3     = ROOT.RooRealVar('C_pvdistsignif3', '(#Xi, #Xi_{b})_{detsign3}' , 0, 5000)
LmC_vtxprob          = ROOT.RooRealVar('C_vtxprob', '(#Xi, #Xi_{b})_{detsign3}' , 0, 1)
                     
LamC_mm              = ROOT.RooRealVar('C_mass'    , 'M(#Lambda #pi^{+}) [GeV]', 2.20, 2.35)
#
# __ __ __ __ __ __ __ __ XI_C VARS __ __ __ __ __ __ __ __
#   
XiC_m                = ROOT.RooRealVar('C_mass_old'    , 'M(#Xi^{#minus} #pi^{+}) [GeV]', 1.45, 2.6)
XiC_pt               = ROOT.RooRealVar('C_pt'          , 'p_{T}(#Xi_{c}) [GeV]'      , 0, 100)
XiC_pv_dist          = ROOT.RooRealVar('C_pvdist'     , '(#Xi, #Xi_{c})_{dist} [cm]' , 0, 500)
XiC_pv_detsign       = ROOT.RooRealVar('C_pvdistsignif2', '(#Xi, #Xi_{c})_{detsign}'  , 0, 5000)
XiC_pv_detsign3      = ROOT.RooRealVar('C_pvdistsignif3', '(#Xi, #Xi_{c})_{detsign3}' , 0, 5000)
XiC_vtxprob          = ROOT.RooRealVar('C_vtxprob', '(#Xi, #Xi_{b})_{detsign3}' , 0, 1)
                      
XiC_pi_ips           = ROOT.RooRealVar('C_PI_ips'   , 'q(#pi_{#Xi})'             , 0, 500)
XiC_pi_charge        = ROOT.RooRealVar('C_PI_charge'   , 'q(#pi_{#Xi})'             , -1, 1)
#
# __ __ __ __ __ __ __ __ B_S VARS __ __ __ __ __ __ __ __
#
B_mass_old           = ROOT.RooRealVar('B_mass_old'     , 'M(D_{s}^{+}#pi^{#minus}) [GeV]' , 5.15, 5.55           )
B_pt                 = ROOT.RooRealVar('B_pt'           , 'p_{T}(B_{s}) [GeV]'     , 0, 100                  )
B_pvdist             = ROOT.RooRealVar('B_pvdist'       , '(B_{s}, PV)_{dist} [cm]', 0, 500                  )
B_pvdistsignif2      = ROOT.RooRealVar('B_pvdistsignif2', '(B_{s}, PV)_{detsign}'  , 0, 5000                 )
B_Cdistsignif2       = ROOT.RooRealVar('B_Cdistsignif2' , '(B_{s}, D_{s})_{detsign}', 0, 5000                )
B_pvdistsignif3      = ROOT.RooRealVar('B_pvdistsignif3', '(B_{s}, PV)_{detsign3}' , 0, 5000                 )
B_vtxprob            = ROOT.RooRealVar('B_vtxprob'      , '(B_{s})_{vtxprob}'      , 0, 1                    )

#
# __ __ __ __ __ __ __ __ COSINE VARS __ __ __ __ __ __ __ __
# 
LA_XIcos2_CL         = ROOT.RooRealVar('LA_XIcos2_CL'  , 'cos(#Lambda, #Xi)'         , -1, 1)
LA_XIcos3_CL         = ROOT.RooRealVar('LA_XIcos3_CL'  , 'cos3(#Lambda, #Xi)'        , -1, 1)

LA_XBcos2_CL         = ROOT.RooRealVar('LA_XBcos2_CL'  , 'cos(#Lambda, #Xi_{b})'     , -1, 1)
LA_XBcos3_CL         = ROOT.RooRealVar('LA_XBcos3_CL'  , 'cos3(#Lambda, #Xi_{b})'    , -1, 1)

XB_pvcos2_Cjp        = ROOT.RooRealVar('XB_pvcos2_Cjp'  , 'cos(#Xi_{b}, PV)'         , -1, 1)
XB_pvcos3_Cjp        = ROOT.RooRealVar('XB_pvcos3_Cjp'  , 'cos3(#Xi_{b}, PV)'        , -1, 1)

XI_XBcos2            = ROOT.RooRealVar('XI_XBcos2'      , 'cos(#Xi_{b}, #Xi)'        , -1, 1)
XI_XBcos3            = ROOT.RooRealVar('XI_XBcos3'      , 'cos3(#Xi_{b}, #Xi)'       , -1, 1)

XI_XBcos2_CV         = ROOT.RooRealVar('XI_XBcos2_CV'   , 'cos(#Xi_{b}, #Xi)'        , -1, 1)
XI_XBcos3_CV         = ROOT.RooRealVar('XI_XBcos3_CV'   , 'cos3(#Xi_{b}, #Xi)'       , -1, 1)

C_pvcos2             = ROOT.RooRealVar('C_pvcos2'  , 'cos(D_{s}, PV)'                , -1, 1)
C_pvcos3             = ROOT.RooRealVar('C_pvcos3'  , 'cos3(D_{s}, PV)'               , -1, 1)

B_pvcos2             = ROOT.RooRealVar('B_pvcos2'  , 'cos(B_{s}, PV)'                , -1, 1)
B_pvcos3             = ROOT.RooRealVar('B_pvcos3'  , 'cos3(B_{s}, PV)'               , -1, 1)

B_Ccos2             = ROOT.RooRealVar('B_Ccos2'    , 'cos(B_{s}, D_{s})'             , -1, 1)
B_Ccos3             = ROOT.RooRealVar('B_Ccos3'    , 'cos3(B_{s}, D{s})'             , -1, 1)

cos_Lam_LamC         = ROOT.RooRealVar('LAM_Ccos2_CL'  , 'cos(#Lambda, #Xi)'         , -1, 1)
cos3_Lam_LamC        = ROOT.RooRealVar('LAM_Ccos3_CL'  , 'cos3(#Lambda, #Xi)'        , -1, 1)

cos_Lam_Xi           = ROOT.RooRealVar('LAM_XIcos2_CL'  , 'cos(#Lambda, #Xi)'        , -1, 1)
cos3_Lam_Xi          = ROOT.RooRealVar('LAM_XIcos3_CL'  , 'cos3(#Lambda, #Xi)'       , -1, 1)

cos_Xi_XiC           = ROOT.RooRealVar('XI_Ccos2'  , 'cos(#Lambda, #Xi)'        , -1, 1)
cos3_Xi_XiC          = ROOT.RooRealVar('XI_Ccos3'  , 'cos3(#Lambda, #Xi)'       , -1, 1)
                     
cos_PV_XiC           = ROOT.RooRealVar('C_pvcos2'  , 'cos(#Xi_{b}, PV)'         , -1, 1)
cos3_PV_XiC          = ROOT.RooRealVar('C_pvcos3'  , 'cos3(#Xi_{b}, PV)'        , -1, 1)
#
# __ __ __ __ __ __ __ __ MONTE-CARLO VARS __ __ __ __ __ __ __ __
#
gdr_MU_P         = ROOT.RooRealVar('gdr_MU_P'    , 'gdr_MU_P'        , 0, 0.2)
gdr_MU_N         = ROOT.RooRealVar('gdr_MU_N'    , 'gdr_MU_N'        , 0, 0.2)

gdr_XI           = ROOT.RooRealVar('gdr_XI'      , 'gdr_XI'          , 0, 3)
gdr_XI_CV        = ROOT.RooRealVar('gdr_XI_CV'   , 'gdr_XI_CV'       , 0, 3)

gdr_Lambda       = ROOT.RooRealVar('gdr_Lambda'  , 'gdr_Lambda'       , 0, 3)
gdr_kaon         = ROOT.RooRealVar('gdr_kaon'    , 'gdr_kaon'         , 0, 3)
gdr_kaon_CV      = ROOT.RooRealVar('gdr_kaon_CV' , 'gdr_kaon_CV'      , 0, 3)

gdr_XB_piP_A     = ROOT.RooRealVar('gdr_XB_piP_A', 'gdr_XB_piP_A'    , 0, 3)
gdr_XB_piP       = ROOT.RooRealVar('gdr_XB_piP'  , 'gdr_XB_piP'      , 0, 3)
gdr_XB_piN_A     = ROOT.RooRealVar('gdr_XB_piN_A', 'gdr_XB_piN_A'    , 0, 3)
gdr_XB_piN       = ROOT.RooRealVar('gdr_XB_piN'  , 'gdr_XB_piN'      , 0, 3)

gdr_XB_XBpi_N_A  = ROOT.RooRealVar('gdr_XB_XBpi_N_A', 'gdr_XB_piN_A'    , 0, 10)
gdr_XB_XBpi_P_A  = ROOT.RooRealVar('gdr_XB_XBpi_P_A', 'gdr_XB_XBpi_P_A' , 0, 10)
gdr_XB_XBpi_X_A  = ROOT.RooRealVar('gdr_XB_XBpi_X_A', 'gdr_XB_XBpi_X_A' , 0, 10)

gpt_XB_piP_A     = ROOT.RooRealVar('gpt_XB_piP_A', 'gpt_XB_piP_A'    , -2, 2)
gpt_XB_piN_A     = ROOT.RooRealVar('gpt_XB_piN_A', 'gpt_XB_piN_A'    , -2, 2)

gen_LA_M         = ROOT.RooRealVar('gen_LA_M'    , 'M^{gen}(#Lambda) [GeV]' , 1, 2)
#
# __ __ __ __ __ __ __ __ TRIGGERS VARS __ __ __ __ __ __ __ __
#
TRIG_Jp25               =   ROOT.RooRealVar('TRIG_Jp25'             , 'TRIG_Jp25'             , 0, 1)
TRIG_Jp20Seag           =   ROOT.RooRealVar('TRIG_Jp20Seag'         , 'TRIG_Jp20Seag'         , 0, 1)
TRIG_JpTrkDisplaced     =   ROOT.RooRealVar('TRIG_JpTrkDisplaced'   , 'TRIG_JpTrkDisplaced'   , 0, 1)
TRIG_JpTrkTrkDisplaced  =   ROOT.RooRealVar('TRIG_JpTrkTrkDisplaced', 'TRIG_JpTrkTrkDisplaced', 0, 1)
TRIG_Jp43isplaced       =   ROOT.RooRealVar('TRIG_Jp43isplaced'     , 'RIG_Jp43isplaced'      , 0, 1)
TRIG_Jp43               =   ROOT.RooRealVar('TRIG_Jp43'             , 'TRIG_Jp43'             , 0, 1)
TRIG_Jp4Displaced       =   ROOT.RooRealVar('TRIG_Jp4Displaced'     , 'TRIG_Jp4Displaced'     , 0, 1)
TRIG_JpMu               =   ROOT.RooRealVar('TRIG_JpMu'             , 'TRIG_JpMu'             , 0, 1)
TRIG_JpPhiMM            =   ROOT.RooRealVar('TRIG_JpPhiMM'          , 'TRIG_JpPhiMM'          , 0, 1)
TRIG_JpPhiKKv2          =   ROOT.RooRealVar('TRIG_JpPhiKKv2'        , 'TRIG_JpPhiKKv2'        , 0, 1)
TRIG_JpPhiKKv4          =   ROOT.RooRealVar('TRIG_JpPhiKKv4'        , 'TRIG_JpPhiKKv4'        , 0, 1)

TRIG_Psip18             =   ROOT.RooRealVar('TRIG_Psip18'           , 'TRIG_Psip18'           , 0, 1)
TRIG_Psip10Seag         =   ROOT.RooRealVar('TRIG_Psip10Seag'       , 'TRIG_Psip10Seag'       , 0, 1)
TRIG_PripTrDisplaced    =   ROOT.RooRealVar('TRIG_PripTrDisplaced'  , 'TRIG_PripTrDisplaced'  , 0, 1)




lumi_13TeV = {2016: 36.1, 2017: 42.1, 2018: 61.6}
lumi_136TeV = {2022: "~5"}


### Tp = Tlab * sqrt(1-v2/c2) = d/v * sqrt(1-v2/c2)
### p = m*v / sqrt(1-v2/c2)
### sqrt(1-v2/c2) = m*v/p
### m2v2c2/p2c2 + v2/c2= 1
### v = c * sqrt(1/(1+m2c2/p2)) [=~ c * (1-m2c2/2p2)]
### Tp = d/v * sqrt(1-1/(1+m2c2/p2))
###


def DetachSignificance2(vtx, vtxE1, vtxE2):
    return sqrt( vtx.X()**2 / (vtxE1.X()**2 + vtxE2.X()**2) + vtx.Y()**2 / (vtxE1.Y()**2 + vtxE2.Y()**2))


def DetachSignificance3(vtx, vtxE1, vtxE2):
    return sqrt( vtx.X()**2 / (vtxE1.X()**2 + vtxE2.X()**2) + vtx.Y()**2 / (vtxE1.Y()**2 + vtxE2.Y()**2) + vtx.Z()**2 / (vtxE1.Z()**2 + vtxE2.Z()**2))


def DirectionCos2 (v1, v2):
    r1 = sqrt(v1.X()**2 + v1.Y()**2)
    r2 = sqrt(v2.X()**2 + v2.Y()**2)
    return ( v1.X() * v2.X() + v1.Y() * v2.Y() ) / (r1*r2 + 0.0000001)


def DirectionCos3(v1, v2):
    r1 = sqrt(v1.X()**2 + v1.Y()**2 + v1.Z()**2)
    r2 = sqrt(v2.X()**2 + v2.Y()**2 + v2.Z()**2)
    return ( v1.X() * v2.X() + v1.Y() * v2.Y() + v1.Z() * v2.Z() ) / (r1*r2 + 0.0000001)


def DirectionChi22(vtx0, vtx0E, vtx1, vtx1E, P, PE):
    dvtx    = vtx1 - vtx0
    dvtxE   = ROOT.TVector3( sqrt(vtx0E.X()**2 + vtx1E.X()**2), sqrt(vtx0E.Y()**2 + vtx1E.Y()**2), sqrt(vtx0E.Z()**2 + vtx1E.Z()**2) )
    Pscaled = P * (dvtx.Mag() / P.Mag())
    PscaledE= PE * (dvtx.Mag() / P.Mag())
    return DetachSignificance2 (Pscaled - dvtx, PscaledE, dvtxE)


def DirectionChi23(vtx0, vtx0E, vtx1, vtx1E, P, PE):
    dvtx    = vtx1 - vtx0 ## vertex difference
    dvtxE   = ROOT.TVector3( sqrt(vtx0E.X()**2 + vtx1E.X()**2), sqrt(vtx0E.Y()**2 + vtx1E.Y()**2), sqrt(vtx0E.Z()**2 + vtx1E.Z()**2) ) ## its error
    Pscaled = P * (dvtx.Mag() / P.Mag()) ## scaled momentum to be the same length as vertex difference
    PscaledE= PE * (dvtx.Mag() / P.Mag()) ## its error
    return DetachSignificance3 (Pscaled - dvtx, PscaledE, dvtxE)


def get_fr_bin(N, var, frame):
    frame_min = frame.GetXaxis().GetXmin()
    frame_max = frame.GetXaxis().GetXmax()
    var_name  = var.GetTitle()

    if var_name[-4:-1] == 'GeV':
        res = round(1000 * (frame_max - frame_min) / N, 3)
        if res.is_integer():
            res = int(res)
        if res < 500:
            return f'{res} MeV'
        else:
            return f'{res / 1000} GeV'
    elif var_name[-4:-1] == 'MeV':
        res = round((frame_max - frame_min) / N, 3)
        if res.is_integer():
            res = int(res)
        if res < 500:
            return f'{res} MeV'
        else:
            return f'{res / 1000} GeV'
    else:
        res = round((frame_max - frame_min) / N, 9)
        if res.is_integer():
            res = int(res)
        return res


def get_yaer(y16, y17, y18, y22):
    cut, per = '', 0
    cut2016 = 'run > 270000 && run < 290000'
    cut2017 = 'run > 290001 && run < 310000'
    cut2018 = 'run > 310001 && run < 330000'
    cut2022 = 'run > 340001 && run < 370000'

    lumi = 0
    
    if y16:
        cut = cut2016
        lumi += lumi_13TeV[2016]
        per = 16
    if y17:
        cut = cut2017
        lumi += lumi_13TeV[2017]
        per = 17
    if y18:
        cut = cut2018
        lumi += lumi_13TeV[2018]
        per = 18

    if y22:
        cut = cut2022
        lumi = lumi_136TeV[2022]
        per = 22
    
    if y16 and y17:
        cut = '((' + cut2016 + ') || (' + cut2017 + '))' 
        per = 1617     
    if y16 and y18:
        cut = '((' + cut2016 + ') || (' + cut2018 + '))'
        per = 1618   
    if y17 and y18:
        cut = '((' + cut2017 + ') || (' + cut2018 + '))'
        per = 1718
    if y16 and y17 and y18:
        cut = '((' + cut2016 + ') || (' + cut2017 + ') || (' + cut2018 + '))'
        per = 4

    try:
        if lumi > 70:
            lumi = round(lumi)
    except TypeError:
        pass
    return cut, lumi, per
    
def get_MC_years(y16, y17, y18):
    year = ''
    if y16:
        year = '2016'
    if y17:
        year = '2017'
    if y18:
        year = '2018'
    
    if y16 and y17:
        year = '2016-2017'     
    if y16 and y18:
        year = '2016+2018' 
    if y17 and y18:
        year = '2017-2018' 
    if y16 and y17 and y18:
        year = '2016-2018' 
    return year

def get_MC_shape_year(y16, y17, y18):
    year = ''
    if y16:
        year = '2016'
    if y17:
        year = '2017'
    if y18:
        year = '2018'

    if y16 and y17 and y18:
        year = 'comb'
    return year
