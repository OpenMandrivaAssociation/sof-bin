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
# due to the upgrade problem, we can't make sof-v* -> sof symlink
cp -a sof-%{version} %{buildroot}%{_firmwaredir}/intel/sof
cp -a sof-tplg-v%{version} %{buildroot}%{_firmwaredir}/intel/
ln -s sof-tplg-v%{version} %{buildroot}%{_firmwaredir}/intel/sof-tplg
%fdupes -s %{buildroot}

%files
%license LICENCE.*
%doc README.*
%{_firmwaredir}/*
