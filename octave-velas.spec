%global octpkg velas

Summary:	VELAS is a user-friendly open-source toolbox for the visualization and analysis
Name:		octave-velas
Version:	1.0.6
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/velas/
Url:		https://github.com/ranzhengcode/VELAS
#Source0:	https://github.com/ranzhengcode/VELAS/archive/refs/tags/v%{version}/%{octpkg}-%{version}.tar.gz
Source0:	https://github.com/ranzhengcode/VELAS/archive/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 5.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
VELAS is a user-friendly open-source toolbox for the visualization 
and analysis of elastic anisotropy written in GNU Octave that can be 
used for any crystal symmetry.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n VELAS-%{version}

# fix version in DESCRIPTION
sed -i -e "s|Version: 1.0.5|Version: %{version}|" DESCRIPTION

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

