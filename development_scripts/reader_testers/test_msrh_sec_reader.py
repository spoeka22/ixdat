"""Demonstrate simple importing and plotting SEC data"""

from pathlib import Path
from ixdat import Measurement

from matplotlib import pyplot as plt

plt.close("all")


data_dir = Path.home() / "Dropbox/ixdat_resources/test_data/sec"

sec_meas = Measurement.read(
    data_dir / "test-7SEC.csv",
    path_to_ref_spec_file=data_dir / "WL.csv",
    path_to_V_J_file=data_dir / "test-7_JV.csv",
    scan_rate=1,
    tstamp=1,
    reader="msrh_sec",
)

sec_meas.calibrate_RE(RE_vs_RHE=0.26)  # provide RE potential in [V] vs RHE
sec_meas.normalize_current(A_el=2)  # provide electrode area in [cm^2]

export_name = "exported_sec.csv"
sec_meas.export(export_name)
ixdat_sec = Measurement.read(export_name, reader="ixdat")
ixdat_sec.plot_measurement(V_ref=0.4, cmap_name="jet")

axes = sec_meas.plot_measurement(
    V_ref=0.4,
    cmap_name="jet",
    make_colorbar=True,
)

ax = sec_meas.plot_waterfall(
    V_ref=0.4,
    cmap_name="jet",
    make_colorbar=True,
)

axes2 = sec_meas.plot_vs_potential(V_ref=0.66, cmap_name="jet", make_colorbar=False)
axes2 = sec_meas.plot_vs_potential(
    V_ref=0.66, vspan=[1.4, 2], cmap_name="jet", make_colorbar=False
)

ax = sec_meas.get_dOD_spectrum(V_ref=0.66, V=1.0).plot(color="b", label="species 1")
sec_meas.get_dOD_spectrum(V_ref=1.0, V=1.45).plot(color="g", ax=ax, label="species 2")
sec_meas.get_dOD_spectrum(V_ref=1.45, V=1.75).plot(color="r", ax=ax, label="species 3")

ax.legend()
