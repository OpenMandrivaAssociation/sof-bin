%global _firmwaredir %{_prefix}/lib/firmware

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2023.09
Release:        1
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildArch:      noarch
  
BuildRequires:  fdupes

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -n sof-bin-%{version}

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}/intel
mkdir -p %{buildroot}%{_bindir}
FW_DEST=%{buildroot}%{_firmwaredir}/intel \
TOOLS_DEST=%{buildroot}%{_bindir} \
rm -rf %{buildroot}%{_bindir}
%fdupes -s %{buildroot}

cp -at /usr/lib/firmware/intel sof*


%files
%license LICENCE.*
%doc README.*
%{_firmwaredir}/*
