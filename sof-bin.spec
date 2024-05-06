%undefine _debugsource_packages
%global _firmwaredir %{_prefix}/lib/firmware

Name:           sof-bin
Summary:        Files for working with SOF firmware
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2024.03
Release:        2
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:	rsync
Requires:	sof-firmware = %{EVRD}

%description
Files for working with SOF firmware

%package -n sof-firmware
Summary:	Various firmware data files for SOF drivers.
Group:		Hardware/Other
BuildArch:	noarch
# FIXME this is weird and should certainly not be necessary, but
# let's see if it fixes updating...
Obsoletes:	sof-firmware < 3.0.0-1

%description -n sof-firmware
Various firmware data files for SOF drivers.

%prep
%autosetup -p1 -n sof-bin-%{version}

%build

%install
mkdir -p "%{buildroot}%{_firmwaredir}/intel" "%{buildroot}%{_bindir}"
FW_DEST="%{buildroot}%{_firmwaredir}/intel" TOOLS_DEST="%{buildroot}%{_bindir}" ./install.sh
%fdupes -s %{buildroot}

%files
%license LICENCE.*
%doc README.*
%{_bindir}/*

%files -n sof-firmware
%{_firmwaredir}/*
